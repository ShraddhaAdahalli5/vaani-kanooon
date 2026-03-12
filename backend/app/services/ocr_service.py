import os
import tempfile
from pathlib import Path
from typing import Optional
import uuid
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from io import BytesIO

from app.config import settings

class OCRService:
    """Service for extracting text from documents using OCR"""
    
    def __init__(self):
        self.supported_image_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
        self.supported_pdf_formats = {'.pdf'}
    
    async def extract_text_from_file(self, file_path: str, file_extension: str) -> str:
        """Extract text from uploaded file"""
        try:
            if file_extension.lower() in self.supported_pdf_formats:
                return await self._extract_from_pdf(file_path)
            elif file_extension.lower() in self.supported_image_formats:
                return await self._extract_from_image(file_path)
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
        except Exception as e:
            raise Exception(f"OCR extraction failed: {str(e)}")
    
    async def _extract_from_pdf(self, file_path: str) -> str:
        """Extract text from PDF file"""
        try:
            # Convert PDF to images
            images = convert_from_path(file_path, dpi=300)
            
            extracted_text = ""
            for i, image in enumerate(images):
                # Extract text from each page
                text = pytesseract.image_to_string(image, lang='eng')
                extracted_text += f"\n--- Page {i+1} ---\n{text}\n"
            
            return extracted_text.strip()
        except Exception as e:
            raise Exception(f"PDF processing failed: {str(e)}")
    
    async def _extract_from_image(self, file_path: str) -> str:
        """Extract text from image file"""
        try:
            # Open and preprocess image
            image = Image.open(file_path)
            
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Extract text using Tesseract
            text = pytesseract.image_to_string(image, lang='eng')
            
            return text.strip()
        except Exception as e:
            raise Exception(f"Image processing failed: {str(e)}")
    
    def _preprocess_image(self, image: Image.Image) -> Image.Image:
        """Preprocess image for better OCR accuracy"""
        # Convert to grayscale
        if image.mode != 'L':
            image = image.convert('L')
        
        # Resize if too small
        width, height = image.size
        if width < 300 or height < 300:
            scale = max(300/width, 300/height)
            new_width = int(width * scale)
            new_height = int(height * scale)
            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        return image
    
    async def save_uploaded_file(self, file_content: bytes, file_extension: str) -> str:
        """Save uploaded file temporarily and return file path"""
        # Create temporary file
        temp_dir = tempfile.gettempdir()
        file_id = str(uuid.uuid4())
        file_path = os.path.join(temp_dir, f"{file_id}{file_extension}")
        
        # Save file
        with open(file_path, 'wb') as f:
            f.write(file_content)
        
        return file_path
    
    def cleanup_temp_file(self, file_path: str):
        """Clean up temporary file"""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception:
            pass  # Ignore cleanup errors

# Create OCR service instance
ocr_service = OCRService()
