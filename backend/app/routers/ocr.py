from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict, Any
import os
import tempfile

from app.models import OCRResponse
from app.services.ocr_service import ocr_service
from app.config import settings

router = APIRouter()

@router.post("/extract", response_model=OCRResponse)
async def extract_text_from_document(file: UploadFile = File(...)):
    """Extract text from uploaded document using OCR"""
    
    # Validate file size
    file_size = 0
    content = await file.read()
    file_size = len(content)
    
    if file_size > settings.max_file_size_bytes:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size is {settings.MAX_FILE_SIZE}"
        )
    
    # Validate file type
    file_extension = os.path.splitext(file.filename)[1].lower()
    supported_extensions = {'.pdf', '.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
    
    if file_extension not in supported_extensions:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type. Supported formats: {', '.join(supported_extensions)}"
        )
    
    try:
        # Save file temporarily
        file_path = await ocr_service.save_uploaded_file(content, file_extension)
        
        try:
            # Extract text using OCR
            extracted_text = await ocr_service.extract_text_from_file(file_path, file_extension)
            
            if not extracted_text.strip():
                return OCRResponse(
                    success=False,
                    extracted_text="",
                    error="No text could be extracted from the document. Please ensure the document contains readable text."
                )
            
            return OCRResponse(
                success=True,
                extracted_text=extracted_text
            )
            
        finally:
            # Clean up temporary file
            ocr_service.cleanup_temp_file(file_path)
            
    except HTTPException:
        raise
    except Exception as e:
        return OCRResponse(
            success=False,
            extracted_text="",
            error=f"OCR processing failed: {str(e)}"
        )

@router.get("/formats")
async def get_supported_formats():
    """Get list of supported file formats"""
    return {
        "success": True,
        "supported_formats": {
            "pdf": [".pdf"],
            "images": [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"]
        },
        "max_file_size": settings.MAX_FILE_SIZE
    }
