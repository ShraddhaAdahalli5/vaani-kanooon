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
    error: Optional[str] = None

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    document_context: str
    conversation_history: Optional[List[ChatMessage]] = []

class ChatResponse(BaseModel):
    success: bool
    response: str
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
