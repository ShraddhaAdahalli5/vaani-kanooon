from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class OCRResponse(BaseModel):
    success: bool
    extracted_text: str
    error: Optional[str] = None

class SimplifyRequest(BaseModel):
    text: str
    target_language: Optional[str] = None

class SimplifyResponse(BaseModel):
    success: bool
    simplified_text: str
    translated_text: Optional[str] = None
    summary: Optional[str] = None
    key_points: Optional[List[str]] = []
    processing_method: Optional[str] = None
    error: Optional[str] = None

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    document_context: str
    target_language: Optional[str] = "hindi"
    conversation_history: Optional[List[ChatMessage]] = []

class ChatResponse(BaseModel):
    success: bool
    response: str
    processing_method: Optional[str] = None
    conversation_id: Optional[str] = None
    error: Optional[str] = None

class Language(BaseModel):
    code: str
    name: str
    native_name: str

class LanguagesResponse(BaseModel):
    success: bool
    languages: List[Language]
    error: Optional[str] = None
