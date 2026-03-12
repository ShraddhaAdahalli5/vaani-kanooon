# Vani-Kanoon – The Legal Bridge

AI-powered Legal Document Translator and Advisor for rural India

## Overview

Vani-Kanoon is a Generative AI-based platform that helps rural citizens in India understand complex legal documents in their regional language. The platform accepts legal documents (PDFs or scanned images), extracts text using OCR, simplifies complex legal English, and translates the explanations into regional languages like Kannada, Hindi, Marathi, Tamil, and Telugu.

## Features

- **Document Upload**: Accept PDF files and scanned images
- **OCR Text Extraction**: Extract text from legal documents
- **AI Simplification**: Simplify complex legal language using AI
- **Multi-language Translation**: Translate to regional Indian languages
- **Interactive Chatbot**: Ask follow-up questions about documents
- **Voice Output**: Audio explanations for accessibility
- **Low-bandwidth Mode**: Optimized for rural connectivity

## Tech Stack

### Frontend
- React 18
- TailwindCSS
- React Router
- Axios for API calls

### Backend
- Python FastAPI
- Tesseract OCR
- OpenAI API
- Translation API

### Deployment
- Frontend: Vercel/Netlify
- Backend: Render/Railway

## Project Structure

```
vaani-kanoon/
├── frontend/          # React frontend application
├── backend/           # FastAPI backend server
├── README.md          # Project documentation
└── .env.example       # Environment variables template
```

## Social Impact

This project addresses the critical need for legal accessibility in rural India, where:
- 70% of rural population has limited English proficiency
- Legal documents are predominantly in complex English
- Access to legal counsel is limited
- Property rights and agreements need better understanding

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.9+
- Tesseract OCR
- OpenAI API key
- (Optional) Google Cloud Translation API key

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/vani-kanoon.git
   cd vani-kanoon
   ```

2. **Run the setup script**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Configure environment variables**
   - Backend: Copy `backend/.env.example` to `backend/.env` and add your OpenAI API key
   - Frontend: Copy `frontend/.env.example` to `frontend/.env` and set your API URL

4. **Start the development servers**
   ```bash
   # Backend (in one terminal)
   cd backend
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   python main.py

   # Frontend (in another terminal)
   cd frontend
   npm start
   ```

### Manual Installation

#### Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Edit with your API keys
python main.py
```

#### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env  # Edit with your API URL
npm start
```

### Using Docker
```bash
# Start all services
docker-compose up --build

# Stop services
docker-compose down
```

## Access Points

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/docs
- **Health Check**: http://localhost:8000/api/health

## Deployment

### Frontend (Vercel)

1. Connect your GitHub repository to Vercel
2. Set environment variable: `REACT_APP_API_URL` to your backend URL
3. Deploy automatically on push to main branch

### Backend (Render)

1. Connect your GitHub repository to Render
2. Set environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `GOOGLE_TRANSLATE_API_KEY`: (Optional) Google Translate API key
   - `DEBUG`: `false`
3. Deploy using the `render.yaml` configuration

### Docker Production

```bash
# Build and run with Docker
docker build -t vani-kanoon .
docker run -p 8000:8000 --env-file .env vani-kanoon
```

### Environment Variables

#### Backend (.env)
```env
OPENAI_API_KEY=sk-your-openai-api-key
GOOGLE_TRANSLATE_API_KEY=your-google-translate-key  # Optional
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=false
MAX_FILE_SIZE=10MB
```

#### Frontend (.env)
```env
REACT_APP_API_URL=https://your-backend-url.com
```

## API Endpoints

### OCR Operations
- `POST /api/ocr/extract` - Extract text from document
- `GET /api/ocr/formats` - Get supported file formats

### AI Operations
- `POST /api/ai/simplify` - Simplify legal text
- `POST /api/ai/chat` - Chat with AI about document
- `GET /api/ai/status` - Check AI service status

### Languages
- `GET /api/languages/` - Get supported languages
- `GET /api/languages/{code}` - Get specific language info

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - See LICENSE file for details
