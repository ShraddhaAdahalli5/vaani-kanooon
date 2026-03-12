from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # API Configuration
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = True
    
    # OpenAI Configuration
    OPENAI_API_KEY: str
    
    # Google Cloud Translation (Optional)
    GOOGLE_TRANSLATE_API_KEY: Optional[str] = None
    
    # File Upload Configuration
    MAX_FILE_SIZE: str = "10MB"
    UPLOAD_DIR: str = "uploads"
    
    # OCR Configuration
    TESSERACT_CMD: Optional[str] = None
    
    # CORS Configuration
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "https://vani-kanoon.vercel.app",
        "https://vani-kanoon.onrender.com",
        "https://vani-kanoon.netlify.app"
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

    @property
    def max_file_size_bytes(self) -> int:
        """Convert max file size string to bytes"""
        size_str = self.MAX_FILE_SIZE.upper()
        if size_str.endswith("MB"):
            return int(size_str[:-2]) * 1024 * 1024
        elif size_str.endswith("KB"):
            return int(size_str[:-2]) * 1024
        else:
            return int(size_str)

# Create global settings instance
settings = Settings()

# Set Tesseract command if specified
if settings.TESSERACT_CMD:
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_CMD
