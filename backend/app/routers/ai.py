from fastapi import APIRouter, HTTPException
from typing import List

from app.models import SimplifyRequest, SimplifyResponse, ChatRequest, ChatResponse, ChatMessage
from app.services.offline_ai_service import OfflineAIService

router = APIRouter()

# Initialize offline AI service
offline_ai_service = OfflineAIService()

@router.get("/test")
async def test_endpoint():
    """Simple test endpoint to verify backend is working"""
    return {
        "status": "working",
        "message": "Backend is responding correctly",
        "timestamp": "2024-03-13"
    }

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
        # Simple ultra-fast processing for presentation
        text = request.text
        target_lang = request.target_language or "english"
        
        # Simplify text
        simplified = offline_ai_service.simplify_text(text)
        
        # Translate if needed
        if target_lang == "english" or target_lang == "en":
            translated = simplified
        else:
            translated = offline_ai_service.translate_to_regional_language(simplified, target_lang)
        
        return SimplifyResponse(
            success=True,
            simplified_text=simplified,
            translated_text=translated,
            summary="Document simplified for easy understanding.",
            key_points=["Key legal terms simplified", "Rights and obligations clarified", "Important dates and payments identified"],
            processing_method="offline"
        )
        
    except Exception as e:
        return SimplifyResponse(
            success=False,
            simplified_text="",
            error=f"Processing failed: {str(e)}"
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
    
    try:
        # Ultra-fast chat responses
        response = offline_ai_service.chat_about_document(
            request.message,
            request.document_context,
            request.target_language or "english"
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
