import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://vaani-kanooon.onrender.com';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface OCRResponse {
  success: boolean;
  extracted_text: string;
  error?: string;
}

export interface SimplifyRequest {
  text: string;
  target_language?: string;
}

export interface SimplifyResponse {
  success: boolean;
  simplified_text: string;
  translated_text?: string;
  summary?: string;
  key_points?: string[];
  processing_method?: string;
  error?: string;
}

export interface ChatRequest {
  message: string;
  document_context: string;
  target_language?: string;
  conversation_history?: Array<{ role: string; content: string }>;
}

export interface ChatResponse {
  success: boolean;
  response: string;
  processing_method?: string;
  conversation_id?: string;
  error?: string;
}

export const documentAPI = {
  // Upload and extract text from document
  uploadDocument: async (file: File): Promise<OCRResponse> => {
    const formData = new FormData();
    formData.append('file', file);
    
    try {
      const response = await api.post('/api/ocr/extract', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      return response.data;
    } catch (error) {
      console.error('Document upload error:', error);
      return {
        success: false,
        extracted_text: '',
        error: 'Failed to upload and process document',
      };
    }
  },

  // Simplify and translate legal text
  simplifyText: async (request: SimplifyRequest): Promise<SimplifyResponse> => {
    try {
      const response = await api.post('/api/ai/simplify', request);
      return response.data;
    } catch (error) {
      console.error('Text simplification error:', error);
      return {
        success: false,
        simplified_text: '',
        error: 'Failed to simplify legal text',
      };
    }
  },

  // Chat with AI about the document
  chatWithAI: async (request: ChatRequest): Promise<ChatResponse> => {
    try {
      const response = await api.post('/api/ai/chat', request);
      return response.data;
    } catch (error) {
      console.error('Chat error:', error);
      return {
        success: false,
        response: '',
        error: 'Failed to get AI response',
      };
    }
  },

  // Get supported languages
  getSupportedLanguages: async () => {
    try {
      const response = await api.get('/api/ai/languages');
      return response.data;
    } catch (error) {
      console.error('Languages fetch error:', error);
      return {
        success: false,
        languages: [],
        error: 'Failed to fetch supported languages',
      };
    }
  },

  // Get AI status
  getAIStatus: async () => {
    try {
      const response = await api.get('/api/ai/status');
      return response.data;
    } catch (error) {
      console.error('AI status fetch error:', error);
      return {
        success: false,
        ai_available: false,
        error: 'Failed to fetch AI status',
      };
    }
  },
};

export default api;
