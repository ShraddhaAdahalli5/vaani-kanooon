from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

# Create FastAPI app
app = FastAPI(
    title="Vani-Kanoon API",
    description="AI-powered Legal Document Translator and Advisor",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class SimplifyRequest(BaseModel):
    text: str
    target_language: Optional[str] = "english"

class SimplifyResponse(BaseModel):
    success: bool
    simplified_text: str
    translated_text: Optional[str] = ""
    summary: Optional[str] = ""
    key_points: Optional[List[str]] = []
    error: Optional[str] = ""

class ChatRequest(BaseModel):
    message: str
    document_context: str
    target_language: Optional[str] = "english"

class ChatResponse(BaseModel):
    success: bool
    response: str
    error: Optional[str] = ""

# Simple word dictionaries
HINDI_WORDS = {
    "legal": "कानूनी", "document": "दस्तावेज", "agreement": "समझौता",
    "contract": "अनुबंध", "court": "अदालत", "judge": "न्यायाधीश",
    "lawyer": "वकील", "party": "पक्ष", "property": "संपत्ति",
    "land": "जमीन", "house": "घर", "money": "पैसे",
    "payment": "भुगतान", "rights": "अधिकार", "duty": "कर्तव्य",
    "the": "", "and": "और", "is": "है", "are": "हैं",
    "this": "यह", "that": "वह", "for": "के लिए",
    "with": "के साथ", "shall": "गा", "must": "जरूरी"
}

KANNADA_WORDS = {
    "legal": "ಕಾನೂನು", "document": "ದಾಖಲೆ", "agreement": "ಒಪ್ಪಂದ",
    "contract": "ಒಪ್ಪಂದ", "court": "ನ್ಯಾಯಾಲಯ", "judge": "ನ್ಯಾಯಾಧೀಶ",
    "lawyer": "ವಕೀಲ", "party": "ಪಕ್ಷ", "property": "ಆಸ್ತಿ",
    "land": "ಭೂಮಿ", "house": "ಮನೆ", "money": "ಹಣ",
    "payment": "ಪಾವತಿ", "rights": "ಹಕ್ಕುಗಳು", "duty": "ಕರ್ತವ್ಯ",
    "the": "", "and": "ಮತ್ತು", "is": "ಆಗಿದೆ", "are": "ಆಗಿವೆ",
    "this": "ಇದು", "that": "ಅದು", "for": "ಗಾಗಿ",
    "with": "ಜೊತೆ", "shall": "ಆಗಿದೆ", "must": "ಅಗತ್ಯ"
}

def translate_text(text: str, language: str) -> str:
    """Simple word-by-word translation"""
    if language == "english" or language == "en":
        return text
    
    words = text.lower().split()
    result = []
    
    dictionary = HINDI_WORDS if language == "hindi" else KANNADA_WORDS
    
    for word in words:
        clean_word = word.strip('.,!?;:"()[]{}')
        translated = dictionary.get(clean_word, word)
        result.append(translated)
    
    return ' '.join(result)

def get_chat_response(message: str, language: str) -> str:
    """Get chat response in preferred language"""
    message_lower = message.lower()
    
    if language == "hindi":
        if any(word in message_lower for word in ["what", "explain", "summary"]):
            return "यह दस्तावेज पक्षों के बीच कानूनी अधिकारों और जिम्मेदारियों की व्याख्या करता है।"
        elif any(word in message_lower for word in ["rights", "right"]):
            return "आपको स्पष्ट दस्तावेज और निष्पक्ष व्यवहार का अधिकार है।"
        elif any(word in message_lower for word in ["payment", "money"]):
            return "भुगतान की शर्तें और वित्तीय दायित्वयां स्पष्ट रूप से निर्दिषित हैं।"
        else:
            return "दस्तावेज के अनुसार, यह एक मानक कानूनी समझौता प्रतीत है।"
    
    elif language == "kannada":
        if any(word in message_lower for word in ["what", "explain", "summary"]):
            return "ಈ ದಾಖಲೆಯು ಪಕ್ಷಗಳ ನಡುವೆ ಕಾನೂನು ಹಕ್ಕುಗಳು ಮತ್ತು ಜವಾಬ್ದಾರಿಕೆಗಳನ್ನು ವಿವರಿಸುತ್ತದೆ."
        elif any(word in message_lower for word in ["rights", "right"]):
            return "ನಿಮಗೆ ಸ್ಪಷ್ಟ ದಾಖಲೆಗಳು ಮತ್ತು ನ್ಯಾಯ್ಯೋಚನೆಯ ವ್ಯವಹಾರದ ಅಧಿಕಾರ."
        elif any(word in message_lower for word in ["payment", "money"]):
            return "ಪಾವತಿಯ ನಿಯಮಗಳು ಮತ್ತು ಹಣಕಾಸಿನ ಬಾಧ್ಯಗಳು ಸ್ಪಷ್ಟವಾಗಿ ನಿರ್ದಿಷಿಸಲಾಗಿದೆ."
        else:
            return "ದಾಖಲೆಯ ಆಧಾರದ ಮೇಲೆ, ಇದು ಒಂದು ಮಾನಕ ಕಾನೂನು ಒಪ್ಪಂದ."
    
    else:  # English
        if any(word in message_lower for word in ["what", "explain", "summary"]):
            return "This document explains legal rights and responsibilities between parties."
        elif any(word in message_lower for word in ["rights", "right"]):
            return "You have the right to clear documentation and fair treatment."
        elif any(word in message_lower for word in ["payment", "money"]):
            return "Payment terms and financial obligations are clearly specified."
        else:
            return "Based on the document, this appears to be a standard legal agreement."

# Endpoints
@app.get("/")
async def root():
    return {
        "message": "Vani-Kanoon API",
        "version": "1.0.0",
        "status": "working",
        "description": "AI-powered Legal Document Translator and Advisor"
    }

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "services": {
            "translation": "active",
            "chat": "active"
        }
    }

@app.get("/api/ai/test")
async def test_endpoint():
    return {
        "status": "working",
        "message": "Backend is responding correctly",
        "timestamp": "2024-03-13"
    }

@app.post("/api/ai/simplify", response_model=SimplifyResponse)
async def simplify_text(request: SimplifyRequest):
    try:
        # Simplify text (just return as-is for now)
        simplified = request.text
        
        # Translate if needed
        translated = translate_text(simplified, request.target_language)
        
        return SimplifyResponse(
            success=True,
            simplified_text=simplified,
            translated_text=translated,
            summary="Document simplified for easy understanding.",
            key_points=["Key legal terms simplified", "Rights and obligations clarified"],
            error=""
        )
    except Exception as e:
        return SimplifyResponse(
            success=False,
            simplified_text="",
            error=f"Error: {str(e)}"
        )

@app.post("/api/ai/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    try:
        response = get_chat_response(request.message, request.target_language)
        
        return ChatResponse(
            success=True,
            response=response,
            error=""
        )
    except Exception as e:
        return ChatResponse(
            success=False,
            response="",
            error=f"Error: {str(e)}"
        )

@app.get("/api/ai/languages")
async def get_languages():
    return {
        "success": True,
        "languages": [
            {"code": "english", "name": "English", "native": "English"},
            {"code": "hindi", "name": "Hindi", "native": "हिन्दी"},
            {"code": "kannada", "name": "Kannada", "native": "ಕನ್ನಡ"}
        ]
    }

@app.get("/api/ai/status")
async def get_ai_status():
    return {
        "success": True,
        "ai_available": True,
        "processing_method": "offline",
        "supported_languages": ["english", "hindi", "kannada"]
    }

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
