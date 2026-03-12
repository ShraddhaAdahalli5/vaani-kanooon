from fastapi import APIRouter

from app.models import Language, LanguagesResponse

router = APIRouter()

@router.get("/", response_model=LanguagesResponse)
async def get_supported_languages():
    """Get list of supported languages for translation"""
    
    languages = [
        Language(
            code="english",
            name="English",
            native_name="English"
        ),
        Language(
            code="kannada",
            name="Kannada",
            native_name="ಕನ್ನಡ"
        ),
        Language(
            code="hindi",
            name="Hindi",
            native_name="हिंदी"
        ),
        Language(
            code="marathi",
            name="Marathi",
            native_name="मराठी"
        ),
        Language(
            code="tamil",
            name="Tamil",
            native_name="தமிழ்"
        ),
        Language(
            code="telugu",
            name="Telugu",
            native_name="తెలుగు"
        )
    ]
    
    return LanguagesResponse(
        success=True,
        languages=languages
    )

@router.get("/{language_code}")
async def get_language_info(language_code: str):
    """Get information about a specific language"""
    
    language_map = {
        "english": {"name": "English", "native_name": "English"},
        "kannada": {"name": "Kannada", "native_name": "ಕನ್ನಡ"},
        "hindi": {"name": "Hindi", "native_name": "हिंदी"},
        "marathi": {"name": "Marathi", "native_name": "मराठी"},
        "tamil": {"name": "Tamil", "native_name": "தமிழ்"},
        "telugu": {"name": "Telugu", "native_name": "తెలుగు"}
    }
    
    if language_code not in language_map:
        return {
            "success": False,
            "error": f"Language '{language_code}' not supported"
        }
    
    return {
        "success": True,
        "language": {
            "code": language_code,
            **language_map[language_code]
        }
    }
