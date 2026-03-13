"""
Offline AI Service for Rural India Legal Document Processing
Works without internet connection, suitable for low-bandwidth areas
"""

import re
import json
from typing import Dict, List, Optional
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class OfflineAIService:
    """Offline AI service for legal document simplification and translation"""
    
    def __init__(self):
        self.legal_terms = self._load_legal_dictionary()
        self.simple_words = self._load_simple_vocabulary()
        self.regional_translations = self._load_regional_translations()
        
    def _load_legal_dictionary(self) -> Dict[str, str]:
        """Load legal term dictionary for simplification"""
        return {
            # Common legal terms
            "plaintiff": "दावेदार" if self.detect_hindi_language() else "ಮೊಕದ್ದಮ್ದಾರ",
            "defendant": "प्रतिवादी" if self.detect_hindi_language() else "ಪ್ರತಿವಾದಿ",
            "jurisdiction": "अधिकार क्षेत्र" if self.detect_hindi_language() else "ಅಧಿಕ್ಷೇತ್ರ",
            "injunction": "निषेधाज्ञा" if self.detect_hindi_language() else "ನಿಷೇಧಾಜ್ಞೆ",
            "subpoena": "समन" if self.detect_hindi_language() else "ಸಮನ್ಸ್",
            "affidavit": "शपथ पत्र" if self.detect_hindi_language() else "ಪ್ರತಿಜ್ಞಾ ಪತ್ರ",
            "litigation": "मुकदमेबाजी" if self.detect_hindi_language() else "ಮೊಕದ್ದಮೆ",
            "evidence": "सबूत" if self.detect_hindi_language() else "ಸಾಕ್ಷಿ",
            "testimony": "गवाही" if self.detect_hindi_language() else "ಸಾಕ್ಷ್ಯ",
            "verdict": "फैसला" if self.detect_hindi_language() else "ತೀರ್ಪು",
            "appeal": "अपील" if self.detect_hindi_language() else "ಅಪೀಲ್",
            "bail": "जमानत" if self.detect_hindi_language() else "ಜಾಮೀನು",
            "warrant": "वारंट" if self.detect_hindi_language() else "ವಾರಂಟ್",
            "contract": "अनुबंध" if self.detect_hindi_language() else "ಒಪ್ಪಂದದ",
            "agreement": "समझौता" if self.detect_hindi_language() else "ಒಪ್ಪಂದ",
            "liability": "दायित्व" if self.detect_hindi_language() else "ಹೊಣೆಗಾರಿಕೆ",
            "damages": "हर्जाना" if self.detect_hindi_language() else "ಪರಿಹಾರ",
            "compensation": "मुआवजा" if self.detect_hindi_language() else "ಪರಿಹಾರ",
            "settlement": "समझौता" if self.detect_hindi_language() else "ರಿಹಾರ",
            "mediation": "मध्यस्थता" if self.detect_hindi_language() else "ಧ್ಯಸ್ಥಿಕೆ",
            "arbitration": "पंचाट" if self.detect_hindi_language() else "ಪಂಚಾಯತಿ",
        }
    
    def _load_simple_vocabulary(self) -> Dict[str, str]:
        """Load simple word replacements"""
        return {
            "whereas": "because",
            "notwithstanding": "despite",
            "heretofore": "until now",
            "thereof": "of that",
            "herein": "in this",
            "wherein": "in which",
            "henceforth": "from now",
            "aforementioned": "mentioned before",
            "subsequent": "after",
            "precedent": "previous case",
            "statute": "law",
            "ordinance": "rule",
            "regulation": "rule",
            "provision": "condition",
            "clause": "section",
            "amendment": "change",
            "repeal": "cancel",
            "enact": "make into law",
            "enforce": "make people follow",
            "comply": "follow",
            "violate": "break",
            "breach": "break",
            "terminate": "end",
            "expire": "end",
            "renew": "continue",
            "extend": "make longer",
            "document": "paper",
            "agreement": "deal",
            "contract": "deal",
            "shall": "must",
            "must": "must",
            "will": "will",
            "may": "can",
            "can": "can",
            "should": "should",
            "could": "could",
            "would": "would",
            "person": "people",
            "party": "side",
            "parties": "sides",
            "court": "court",
            "judge": "judge",
            "lawyer": "lawyer",
            "case": "case",
            "evidence": "proof",
            "witness": "witness",
            "justice": "justice",
            "rights": "rights",
            "duty": "duty",
            "property": "property",
            "land": "land",
            "house": "house",
            "money": "money",
            "loan": "loan",
            "interest": "interest",
            "payment": "payment",
            "fine": "fine",
            "punishment": "punishment",
            "prison": "jail",
            "freedom": "freedom",
            "equality": "equality",
            "the": "the",
            "and": "and",
            "or": "or",
            "but": "but",
            "if": "if",
            "when": "when",
            "where": "where",
            "why": "why",
            "how": "how",
            "what": "what",
            "who": "who",
            "which": "which",
            "this": "this",
            "that": "that",
            "these": "these",
            "those": "those",
            "is": "is",
            "are": "are",
            "was": "was",
            "were": "were",
            "be": "be",
            "been": "been",
            "being": "being",
            "have": "have",
            "has": "has",
            "had": "had",
            "do": "do",
            "does": "does",
            "did": "did",
            "will": "will",
            "would": "would",
            "shall": "shall",
            "should": "should",
            "can": "can",
            "could": "could",
            "may": "may",
            "might": "might",
            "must": "must",
            "ought": "ought",
            "i": "i",
            "you": "you",
            "he": "he",
            "she": "she",
            "it": "it",
            "we": "we",
            "they": "they",
            "me": "me",
            "him": "him",
            "her": "her",
            "us": "us",
            "them": "them",
            "my": "my",
            "your": "your",
            "his": "his",
            "her": "her",
            "its": "its",
            "our": "our",
            "their": "their",
            "mine": "mine",
            "yours": "yours",
            "hers": "hers",
            "ours": "ours",
            "theirs": "theirs",
        }
    
    def _load_regional_translations(self) -> Dict[str, Dict[str, str]]:
        """Load regional language translations"""
        return {
            "hindi": {
                "legal document": "कानूनी दस्तावेज",
                "court": "अदालत",
                "judge": "न्यायाधीश",
                "lawyer": "वकील",
                "case": "मुकदमा",
                "evidence": "सबूत",
                "witness": "गवाह",
                "justice": "न्याय",
                "rights": "अधिकार",
                "duty": "कर्तव्य",
                "agreement": "समझौता",
                "contract": "अनुबंध",
                "property": "संपत्ति",
                "land": "जमीन",
                "house": "घर",
                "money": "पैसे",
                "loan": "कर्ज",
                "interest": "व्याज",
                "payment": "भरणे",
                "fine": "दंड",
                "punishment": "शिक्षा",
                "prison": "तुरुंग",
                "freedom": "स्वातंत्र्य",
                "equality": "समानता",
                "document": "दस्तावेज",
                "paper": "कागज",
                "deal": "सौदा",
                "must": "जरूरी",
                "can": "सकता",
                "will": "करेगा",
                "people": "लोग",
                "side": "पक्ष",
                "proof": "सबूत",
                "jail": "जेल",
                "the": "",
                "and": "और",
                "or": "या",
                "but": "लेकिन",
                "if": "अगर",
                "when": "जब",
                "where": "कहां",
                "why": "क्यों",
                "how": "कैसे",
                "what": "क्या",
                "who": "कौन",
                "this": "यह",
                "that": "वह",
                "is": "है",
                "are": "हैं",
                "was": "था",
                "were": "थे",
                "have": "है",
                "has": "है",
                "had": "था",
                "do": "करो",
                "does": "करता",
                "did": "किया",
                "i": "मैं",
                "you": "तुम",
                "he": "वह",
                "she": "वह",
                "we": "हम",
                "they": "वे",
                "my": "मेरा",
                "your": "तुम्हारा",
                "his": "उसका",
                "her": "उसकी",
                "our": "हमारा",
                "their": "उनका",
            },
            "kannada": {
                "legal document": "ಕಾನೂನು ದಾಖಲೆ",
                "court": "ನ್ಯಾಯಾಲಯ",
                "judge": "ನ್ಯಾಯಾಧೀಶ",
                "lawyer": "ವಕೀಲ",
                "case": "ಪ್ರಕರಣ",
                "evidence": "ಸಾಕ್ಷಿ",
                "witness": "ಸಾಕ್ಷಿ",
                "justice": "ನ್ಯಾಯ",
                "rights": "ಹಕ್ಕುಗಳು",
                "duty": "ಕರ್ತವ್ಯ",
                "agreement": "ಒಪ್ಪಂದ",
                "contract": "ಒಪ್ಪಂದ",
                "property": "ಆಸ್ತಿ",
                "land": "ಭೂಮಿ",
                "house": "ಮನೆ",
                "money": "ಹಣ",
                "loan": "ಸಾಲ",
                "interest": "ಬಡ್ಡಿ",
                "payment": "ಪಾವತಿ",
                "fine": "ದಂಡ",
                "punishment": "ಶಿಕ್ಷೆ",
                "prison": "ಜೈಲು",
                "freedom": "ಸ್ವಾತಂತ್ರ್ಯ",
                "equality": "ಸಮಾನತೆ",
                "document": "ದಾಖಲೆ",
                "paper": "ಕಾಗದ",
                "deal": "ಒಪ್ಪಂದ",
                "must": "ಅಗತ್ಯ",
                "can": "ಸಾಧ್ಯ",
                "will": "ಮಾಡುತ್ತದೆ",
                "people": "ಜನರು",
                "side": "ಪಕ್ಷ",
                "proof": "ಸಾಬೀತು",
                "jail": "ಜೈಲು",
                "the": "",
                "and": "ಮತ್ತು",
                "or": "ಅಥವಾ",
                "but": "ಆದರೆ",
                "if": "ಆದರೆ",
                "when": "ಯಾವಾಗ",
                "where": "ಎಲ್ಲಿ",
                "why": "ಏಕೆ",
                "how": "ಹೇಗೆ",
                "what": "ಏನು",
                "who": "ಯಾರು",
                "this": "ಇದು",
                "that": "ಅದು",
                "is": "ಆಗಿದೆ",
                "are": "ಆಗಿವೆ",
                "was": "ಆಗಿತ್ತು",
                "were": "ಆಗಿದ್ದವು",
                "have": "ಹೊಂದಿದೆ",
                "has": "ಹೊಂದಿದೆ",
                "had": "ಹೊಂದಿತ್ತು",
                "do": "ಮಾಡು",
                "does": "ಮಾಡುತ್ತದೆ",
                "did": "ಮಾಡಿದರು",
                "i": "ನಾನು",
                "you": "ನೀವು",
                "he": "ಅವನು",
                "she": "ಅವಳು",
                "we": "ನಾವು",
                "they": "ಅವರು",
                "my": "ನನ್ನ",
                "your": "ನಿಮ್ಮ",
                "his": "ಅವನ",
                "her": "ಅವಳ",
                "our": "ನಮ್ಮ",
                "their": "ಅವರ",
            },
            "marathi": {
                "legal document": "कायदेशीर दस्तऐवज",
                "court": "न्यायालय",
                "judge": "न्यायाधीश",
                "lawyer": "वकील",
                "case": "खटला",
                "evidence": "पुराव्य",
                "witness": "साक्षीदार",
                "justice": "न्याय",
                "rights": "हक्क",
                "duty": "कर्तव्य",
                "agreement": "करार",
                "contract": "करार",
                "property": "मालमत्ता",
                "land": "जमीन",
                "house": "घर",
                "money": "पैसे",
                "loan": "कर्ज",
                "interest": "व्याज",
                "payment": "भरणे",
                "fine": "दंड",
                "punishment": "शिक्षा",
                "prison": "तुरुंग",
                "freedom": "स्वातंत्र्य",
                "equality": "समानता",
            },
            "tamil": {
                "legal document": "சட்ட ஆவணம்",
                "court": "நீதிமன்றம்",
                "judge": "நீதிபதி",
                "lawyer": "வழக்கறிஞர்",
                "case": "வழக்கு",
                "evidence": "சான்று",
                "witness": "சாட்சி",
                "justice": "நீதி",
                "rights": "உரிமைகள்",
                "duty": "கடமை",
                "agreement": "ஒப்பந்தம்",
                "contract": "ஒப்பந்தம்",
                "property": "சொத்து",
                "land": "நிலம்",
                "house": "வீடு",
                "money": "பணம்",
                "loan": "கடன்",
                "interest": "வட்டி",
                "payment": "செலுத்துதல்",
                "fine": "அபராதம்",
                "punishment": "தண்டனை",
                "prison": "சிறை",
                "freedom": "சுதந்திரம்",
                "equality": "சமத்துவம்",
            },
            "telugu": {
                "legal document": "చట్టపరమైన పత్రం",
                "court": "కోర్టు",
                "judge": "న్యాయాధికారి",
                "lawyer": "న్యాయవాది",
                "case": "కేసు",
                "evidence": "ఆధారం",
                "witness": "సాక్షి",
                "justice": "న్యాయం",
                "rights": "హక్కులు",
                "duty": "విధి",
                "agreement": "ఒప్పందం",
                "contract": "ఒప్పందం",
                "property": "ఆస్తి",
                "land": "భూమి",
                "house": "ఇల్లు",
                "money": "డబ్బు",
                "loan": "రుణం",
                "interest": "వడ్డీ",
                "payment": "చెల్లింపు",
                "fine": "జరిమానా",
                "punishment": "శిక్ష",
                "prison": "జైలు",
                "freedom": "స్వేచ్ఛ",
                "equality": "సమానత్వం",
            }
        }
    
    def detect_hindi_language(self) -> bool:
        """Simple detection for Hindi (fallback)"""
        return True  # Default to Hindi for simplicity
    
    def simplify_text(self, text: str) -> str:
        """Simplify legal text using offline dictionary"""
        if not text:
            return ""
        
        # Convert to lowercase for matching
        simplified = text.lower()
        
        # Replace legal terms with simpler terms
        for legal_term, simple_term in self.legal_terms.items():
            simplified = re.sub(r'\b' + re.escape(legal_term) + r'\b', simple_term, simplified, flags=re.IGNORECASE)
        
        # Replace complex words with simpler ones
        for complex_word, simple_word in self.simple_words.items():
            simplified = re.sub(r'\b' + re.escape(complex_word) + r'\b', simple_word, simplified, flags=re.IGNORECASE)
        
        # Break long sentences
        sentences = simplified.split('. ')
        simplified_sentences = []
        
        for sentence in sentences:
            if len(sentence) > 100:  # If sentence is too long
                # Break it into smaller parts
                words = sentence.split()
                current_sentence = ""
                for word in words:
                    if len(current_sentence + word) < 80:
                        current_sentence += word + " "
                    else:
                        simplified_sentences.append(current_sentence.strip())
                        current_sentence = word + " "
                if current_sentence:
                    simplified_sentences.append(current_sentence.strip())
            else:
                simplified_sentences.append(sentence.strip())
        
        return '. '.join(simplified_sentences)
    
    def translate_to_regional_language(self, text: str, target_language: str) -> str:
        """Ultra-fast translation using optimized processing"""
        if not text:
            return ""
        
        # Early return for English - no translation needed
        if target_language == "english" or target_language == "en":
            return text
        
        if target_language not in self.regional_translations:
            return text  # Return original if language not supported
        
        translations = self.regional_translations[target_language]
        
        # For very short texts, process immediately
        if len(text) < 50:
            return self._translate_short_text(text, translations)
        
        # For longer texts, use sentence-based processing
        sentences = text.split('. ')
        translated_sentences = []
        
        for sentence in sentences:
            if sentence.strip():
                translated_sentence = self._translate_sentence(sentence.strip(), translations)
                translated_sentences.append(translated_sentence)
        
        return '. '.join(translated_sentences)
    
    def _translate_short_text(self, text: str, translations: Dict[str, str]) -> str:
        """Fast translation for short texts"""
        words = text.split()
        translated_words = []
        
        for word in words:
            clean_word = word.lower().strip('.,!?;:"()[]{}')
            if clean_word in translations:
                translated_words.append(translations[clean_word])
            else:
                translated_words.append(word)
        
        return ' '.join(translated_words)
    
    def _translate_sentence(self, sentence: str, translations: Dict[str, str]) -> str:
        """Fast sentence translation"""
        words = sentence.split()
        translated_words = []
        
        for word in words:
            clean_word = word.lower().strip('.,!?;:"()[]{}')
            if clean_word in translations:
                translated_words.append(translations[clean_word])
            else:
                translated_words.append(word)
        
        return ' '.join(translated_words)
    
    def get_supported_languages(self) -> List[Dict[str, str]]:
        """Get list of supported regional languages"""
        return [
            {"code": "english", "name": "English", "native": "English"},
            {"code": "hindi", "name": "हिन्दी (Hindi)", "native": "हिन्दी"},
            {"code": "kannada", "name": "ಕನ್ನಡ (Kannada)", "native": "ಕನ್ನಡ"},
            {"code": "marathi", "name": "मराठी (Marathi)", "native": "मराठी"},
            {"code": "tamil", "name": "தமிழ் (Tamil)", "native": "தமிழ்"},
            {"code": "telugu", "name": "తెలుగు (Telugu)", "native": "తెలుగు"},
        ]
    
    def process_legal_document(self, text: str, target_language: str = "hindi") -> Dict[str, str]:
        """Complete offline processing of legal document"""
        try:
            # Step 1: Simplify the legal text
            simplified_text = self.simplify_text(text)
            
            # Step 2: Translate to regional language (optimized)
            translated_text = ""
            if target_language == "english" or target_language == "en":
                # Fast path for English - no translation needed
                translated_text = simplified_text
            else:
                # Only translate if not English and language is supported
                if target_language in self.regional_translations:
                    translated_text = self.translate_to_regional_language(simplified_text, target_language)
                else:
                    translated_text = simplified_text
            
            # Step 3: Generate summary (simple approach)
            summary = self._generate_simple_summary(simplified_text)
            
            # Step 4: Extract key points
            key_points = self._extract_key_points(simplified_text)
            
            return {
                "original_text": text,
                "simplified_text": simplified_text,
                "translated_text": translated_text,
                "summary": summary,
                "key_points": key_points,
                "language": target_language,
                "processing_method": "offline",
                "confidence": "high"
            }
            
        except Exception as e:
            logger.error(f"Error processing document: {str(e)}")
            return {
                "error": f"Processing failed: {str(e)}",
                "original_text": text,
                "simplified_text": text,
                "translated_text": text,
                "processing_method": "offline",
                "confidence": "low"
            }
    
    def _generate_simple_summary(self, text: str) -> str:
        """Generate a simple summary of the text"""
        # Simple approach: extract first few sentences and key terms
        sentences = text.split('. ')
        if len(sentences) > 3:
            summary = '. '.join(sentences[:3]) + "."
        else:
            summary = text
        
        # Add key legal terms found
        legal_terms_found = []
        for term in self.legal_terms.keys():
            if term.lower() in text.lower():
                legal_terms_found.append(term)
        
        if legal_terms_found:
            summary += f"\n\nKey legal terms: {', '.join(legal_terms_found[:5])}"
        
        return summary
    
    def _extract_key_points(self, text: str) -> List[str]:
        """Extract key points from the text"""
        key_points = []
        
        # Look for important patterns
        patterns = [
            r"the (court|judge|lawyer) (said|ruled|decided)",
            r"(plaintiff|defendant) (must|shall|will)",
            r"(contract|agreement) (states|provides)",
            r"(payment|fine|penalty) (of|is)",
            r"(rights|duties|obligations) (include|are)",
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                # Find the full sentence containing this match
                sentences = text.split('. ')
                for sentence in sentences:
                    if match[0].lower() in sentence.lower():
                        key_points.append(sentence.strip())
                        break
        
        # Return top 5 key points
        return key_points[:5] if key_points else ["Key points extraction not available in offline mode"]
    
    def chat_about_document(self, message: str, document_context: str, target_language: str = "hindi") -> str:
        """Chat about the document using offline responses"""
        try:
            # Simple keyword-based responses for common questions
            message_lower = message.lower()
            context_lower = document_context.lower()
            
            # Check for common question patterns
            if any(word in message_lower for word in ["what", "explain", "summary", "about"]):
                return self._generate_document_summary(document_context, target_language)
            
            elif any(word in message_lower for word in ["rights", "right", "obligation", "duty"]):
                return self._extract_rights_duties(document_context, target_language)
            
            elif any(word in message_lower for word in ["payment", "money", "cost", "fee", "fine"]):
                return self._extract_financial_info(document_context, target_language)
            
            elif any(word in message_lower for word in ["date", "time", "when", "deadline"]):
                return self._extract_dates(document_context, target_language)
            
            elif any(word in message_lower for word in ["court", "judge", "legal", "law"]):
                return self._extract_legal_info(document_context, target_language)
            
            else:
                # Default response for other questions
                return self._generate_default_response(document_context, target_language)
                
        except Exception as e:
            logger.error(f"Error in offline chat: {str(e)}")
            return f"I'm sorry, I'm having trouble understanding your question in offline mode. Please try rephrasing it or check the document summary."
    
    def _generate_document_summary(self, context: str, language: str) -> str:
        """Generate a simple document summary"""
        summary = self._generate_simple_summary(context)
        if language != "english":
            summary = self.translate_to_regional_language(summary, language)
        return f"Document Summary: {summary}"
    
    def _extract_rights_duties(self, context: str, language: str) -> str:
        """Extract rights and duties from document"""
        rights_patterns = [
            r"(right|rights) (to|of|shall|must|will)",
            r"(obligation|duty|duties) (to|of|shall|must|will)",
            r"(responsible|responsible for)",
        ]
        
        found_items = []
        for pattern in rights_patterns:
            matches = re.findall(pattern, context, re.IGNORECASE)
            for match in matches:
                # Find the full sentence
                sentences = context.split('. ')
                for sentence in sentences:
                    if match[0].lower() in sentence.lower():
                        found_items.append(sentence.strip())
                        break
        
        if found_items:
            result = "Rights and Obligations found:\n" + "\n".join(found_items[:3])
        else:
            result = "No specific rights or obligations found in the document."
        
        if language != "english":
            result = self.translate_to_regional_language(result, language)
        
        return result
    
    def _extract_financial_info(self, context: str, language: str) -> str:
        """Extract financial information"""
        money_patterns = [
            r"(\$|₹|rs.|rupees|amount) [\d,]+",
            r"[\d,]+ (rs.|rupees|dollars)",
            r"(payment|fee|fine|penalty|cost) [\d,]+",
        ]
        
        found_items = []
        for pattern in money_patterns:
            matches = re.findall(pattern, context, re.IGNORECASE)
            for match in matches:
                # Find the full sentence
                sentences = context.split('. ')
                for sentence in sentences:
                    if match in sentence:
                        found_items.append(sentence.strip())
                        break
        
        if found_items:
            result = "Financial Information:\n" + "\n".join(found_items[:3])
        else:
            result = "No specific financial amounts found in the document."
        
        if language != "english":
            result = self.translate_to_regional_language(result, language)
        
        return result
    
    def _extract_dates(self, context: str, language: str) -> str:
        """Extract date information"""
        date_patterns = [
            r"\d{1,2}[-/]\d{1,2}[-/]\d{2,4}",
            r"\d{1,2} (january|february|march|april|may|june|july|august|september|october|november|december) \d{2,4}",
            r"(date|due|deadline) (on|by|before|after) [\d\w\s,]+",
        ]
        
        found_items = []
        for pattern in date_patterns:
            matches = re.findall(pattern, context, re.IGNORECASE)
            for match in matches:
                # Find the full sentence
                sentences = context.split('. ')
                for sentence in sentences:
                    if match in sentence:
                        found_items.append(sentence.strip())
                        break
        
        if found_items:
            result = "Important Dates:\n" + "\n".join(found_items[:3])
        else:
            result = "No specific dates found in the document."
        
        if language != "english":
            result = self.translate_to_regional_language(result, language)
        
        return result
    
    def _extract_legal_info(self, context: str, language: str) -> str:
        """Extract legal information"""
        legal_patterns = [
            r"(court|judge|justice) (said|ruled|ordered|decided)",
            r"(law|statute|act|code) (requires|states|provides)",
            r"(legal|illegal|unlawful) (action|act|behavior)",
        ]
        
        found_items = []
        for pattern in legal_patterns:
            matches = re.findall(pattern, context, re.IGNORECASE)
            for match in matches:
                # Find the full sentence
                sentences = context.split('. ')
                for sentence in sentences:
                    if match[0].lower() in sentence.lower():
                        found_items.append(sentence.strip())
                        break
        
        if found_items:
            result = "Legal Information:\n" + "\n".join(found_items[:3])
        else:
            result = "No specific legal proceedings mentioned in the document."
        
        if language != "english":
            result = self.translate_to_regional_language(result, language)
        
        return result
    
    def _generate_default_response(self, context: str, language: str) -> str:
        """Generate a default response"""
        if language == "hindi":
            return "मैं आपके प्रश्न को पूरी तरह से नहीं समझ पाया। कृपया दस्तावेज़ के सारांश देखें या अपना प्रश्न फिर से लिखें।"
        elif language == "kannada":
            return "ನಾನು ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಅರ್ಥಮಾಡಲಿಲ್ಲ. ದಯವಿಟ್ಟು ದಾಖಲೆಯ ಸಾರಾಂಶವನ್ನು ನೋಡಿ ಅಥವಾ ನಿಮ್ಮ ಪ್ರಶ್ನೆಯನ್ನು ಮರುಬರೆಯಿರಿ."
        elif language == "marathi":
            return "मी तुमच्या प्रश्नाचे पूर्णपणे अर्थ लावू शकलो नाही. कृपया दस्तऐवजाचा सारांश पहा किंवा तुमचा प्रश्न पुन्हा लिहा."
        elif language == "tamil":
            return "நான் உங்கள் கேள்வியை முழுமையாக புரிந்து கொள்ளவில்லை. தயவுசெய்து ஆவணத்தின் சுருக்கத்தைப் பார்க்கவும் அல்லது உங்கள் கேள்வியை மீண்டும் எழுதவும்."
        elif language == "telugu":
            return "నేను మీ ప్రశ్నను పూర్తిగా అర్థం చేసుకోలేకపోయాను. దయచేసి పత్రం సారాంశాన్ని చూడండి లేదా మీ ప్రశ్నను తిరిగి రాయండి."
        else:
            return "I don't fully understand your question. Please review the document summary or try rephrasing your question."
