from fastapi import APIRouter, HTTPException
from typing import List

from app.models import SimplifyRequest, SimplifyResponse, ChatRequest, ChatResponse, ChatMessage
from app.services.ai_service import ai_service

router = APIRouter()

@router.post("/simplify", response_model=SimplifyResponse)
async def simplify_legal_text(request: SimplifyRequest):
    """Simplify legal text and optionally translate to target language"""
    
    if not ai_service:
        return SimplifyResponse(
            success=False,
            simplified_text="",
            error="AI service is not available. Please configure OpenAI API key."
        )
    
    if not request.text or not request.text.strip():
        return SimplifyResponse(
            success=False,
            simplified_text="",
            error="No text provided for simplification."
        )
    
    try:
        simplified_text, translated_text = await ai_service.simplify_legal_text(
            request.text, 
            request.target_language
        )
        
        return SimplifyResponse(
            success=True,
            simplified_text=simplified_text,
            translated_text=translated_text
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
    
    if not ai_service:
        return ChatResponse(
            success=False,
            response="",
            error="AI service is not available. Please configure OpenAI API key."
        )
    
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
        # Convert Pydantic models to dict for AI service
        conversation_history = []
        if request.conversation_history:
            conversation_history = [
                ChatMessage(role=msg.role, content=msg.content)
                for msg in request.conversation_history
            ]
        
        response = await ai_service.chat_about_document(
            request.message,
            request.document_context,
            conversation_history
        )
        
        return ChatResponse(
            success=True,
            response=response
        )
        
    except Exception as e:
        return ChatResponse(
            success=False,
            response="",
            error=f"Chat failed: {str(e)}"
        )

@router.get("/status")
async def get_ai_status():
    """Check AI service status"""
    return {
        "success": True,
        "ai_available": ai_service is not None,
        "services": {
            "text_simplification": ai_service is not None,
            "translation": ai_service is not None,
            "chat": ai_service is not None
        }
    }
