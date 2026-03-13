from fastapi import APIRouter, HTTPException
from typing import List

from app.models import SimplifyRequest, SimplifyResponse, ChatRequest, ChatResponse, ChatMessage
from app.services.ai_service import ai_service
from app.services.offline_ai_service import OfflineAIService

router = APIRouter()

# Initialize offline AI service
offline_ai_service = OfflineAIService()

@router.post("/simplify", response_model=SimplifyResponse)
async def simplify_legal_text(request: SimplifyRequest):
    """Simplify legal text and optionally translate to target language"""
    
    if not request.text or not request.text.strip():
        return SimplifyResponse(
            success=False,
            simplified_text="",
            error="No text provided for simplification."
        )
    
    try:
        # Try offline service first (for rural areas)
        result = offline_ai_service.process_legal_document(
            request.text, 
            request.target_language or "english"  # Default to English, not Hindi
        )
        
        return SimplifyResponse(
            success=True,
            simplified_text=result.get("simplified_text", ""),
            translated_text=result.get("translated_text", ""),
            summary=result.get("summary", ""),
            key_points=result.get("key_points", []),
            processing_method="offline"
        )
        
    except Exception as e:
        return SimplifyResponse(
            success=False,
            simplified_text="",
            error=f"AI processing failed: {str(e)}"
        )

@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """Chat with AI about the document"""
    
    if not request.message or not request.message.strip():
        return ChatResponse(
            success=False,
            response="",
            error="No message provided."
        )
    
    if not request.document_context or not request.document_context.strip():
        return ChatResponse(
            success=False,
            response="",
            error="No document context provided."
        )
    
    try:
        # Use offline chat service for rural areas
        response = offline_ai_service.chat_about_document(
            request.message,
            request.document_context,
            request.target_language or "hindi"
        )
        
        return ChatResponse(
            success=True,
            response=response,
            processing_method="offline"
        )
        
    except Exception as e:
        return ChatResponse(
            success=False,
            response="",
            error=f"Chat failed: {str(e)}"
        )

@router.get("/languages", response_model=LanguagesResponse)
async def get_supported_languages():
    """Get list of supported regional languages"""
    try:
        languages = offline_ai_service.get_supported_languages()
        return LanguagesResponse(
            success=True,
            languages=[
                Language(code=lang["code"], name=lang["name"], native_name=lang["native"])
                for lang in languages
            ]
        )
    except Exception as e:
        return LanguagesResponse(
            success=False,
            languages=[],
            error=f"Failed to get languages: {str(e)}"
        )

@router.get("/status")
async def get_ai_status():
    """Check AI service status"""
    return {
        "success": True,
        "ai_available": True,
        "processing_method": "offline",
        "services": {
            "text_simplification": True,
            "translation": True,
            "chat": True,
            "ocr": True
        },
        "supported_languages": offline_ai_service.get_supported_languages(),
        "internet_required": False,
        "rural_compatible": True
    }
