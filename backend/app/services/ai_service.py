import openai
from typing import Optional, List, Dict, Any
import json

from app.config import settings
from app.models import ChatMessage

class AIService:
    """Service for AI-powered text simplification and chat"""
    
    def __init__(self):
        if not settings.OPENAI_API_KEY:
            raise ValueError("OpenAI API key is required")
        
        openai.api_key = settings.OPENAI_API_KEY
        self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
    
    async def simplify_legal_text(self, text: str, target_language: Optional[str] = None) -> tuple[str, Optional[str]]:
        """Simplify legal text and optionally translate to target language"""
        try:
            # First, simplify the legal text
            simplified_text = await self._simplify_text(text)
            
            # Then translate if target language is specified
            translated_text = None
            if target_language and target_language != 'english':
                translated_text = await self._translate_text(simplified_text, target_language)
            
            return simplified_text, translated_text
        except Exception as e:
            raise Exception(f"AI processing failed: {str(e)}")
    
    async def _simplify_text(self, text: str) -> str:
        """Simplify complex legal text using AI"""
        prompt = f"""
You are a legal expert who specializes in simplifying complex legal documents for rural Indian citizens who have limited legal knowledge and English proficiency.

Please simplify the following legal text by:
1. Breaking down complex legal terms into simple, everyday language
2. Explaining rights and obligations clearly
3. Highlighting important points and potential risks
4. Using simple sentence structure
5. Adding section headers for clarity

Legal Text:
{text}

Provide the simplified explanation in a clear, structured format with appropriate headers and bullet points.
Focus on practical implications and what the document means for the average person.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a legal expert who simplifies complex legal documents for ordinary people."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.3
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"Text simplification failed: {str(e)}")
    
    async def _translate_text(self, text: str, target_language: str) -> str:
        """Translate text to target language"""
        language_map = {
            'kannada': 'Kannada',
            'hindi': 'Hindi',
            'marathi': 'Marathi',
            'tamil': 'Tamil',
            'telugu': 'Telugu'
        }
        
        target_lang_name = language_map.get(target_language.lower(), target_language)
        
        prompt = f"""
Translate the following text to {target_lang_name}. The text contains legal explanations that should be translated accurately while maintaining simplicity and clarity.

Text to translate:
{text}

Provide only the translation without any additional commentary.
"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a professional translator specializing in legal documents from English to {target_lang_name}."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.3
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"Translation failed: {str(e)}")
    
    async def chat_about_document(self, message: str, document_context: str, conversation_history: List[ChatMessage] = None) -> str:
        """Chat with AI about the document"""
        if conversation_history is None:
            conversation_history = []
        
        # Build conversation history for OpenAI
        messages = [
            {"role": "system", "content": f"""
You are a legal assistant helping rural Indian citizens understand their legal documents. 
You have access to the following document context:

Document Context:
{document_context}

Your role is to:
1. Answer questions about the document in simple, clear language
2. Explain legal rights and obligations
3. Highlight potential risks or important considerations
4. Be helpful, patient, and thorough
5. If you're unsure about something, recommend consulting a legal professional

Always provide practical, actionable advice in simple terms.
"""}
        ]
        
        # Add conversation history
        for msg in conversation_history[-5:]:  # Limit to last 5 messages to avoid token limits
            messages.append({"role": msg.role, "content": msg.content})
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=1000,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"Chat response failed: {str(e)}")

# Create AI service instance
try:
    ai_service = AIService()
except ValueError:
    # AI service not available without API key
    ai_service = None
