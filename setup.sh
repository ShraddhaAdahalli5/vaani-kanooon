#!/bin/bash

# Vani-Kanoon Setup Script
echo "🚀 Setting up Vani-Kanoon - The Legal Bridge..."

# Check prerequisites
echo "📋 Checking prerequisites..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ first."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3.9+ is not installed. Please install Python first."
    exit 1
fi

# Check if Tesseract OCR is installed
if ! command -v tesseract &> /dev/null; then
    echo "⚠️  Tesseract OCR is not installed."
    echo "📥 Installing Tesseract OCR..."
    
    # Detect OS and install accordingly
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            brew install tesseract
        else
            echo "❌ Homebrew not found. Please install Homebrew first."
            exit 1
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        sudo apt-get update
        sudo apt-get install -y tesseract-ocr tesseract-ocr-eng
    else
        echo "❌ Unsupported OS. Please install Tesseract OCR manually."
        exit 1
    fi
fi

echo "✅ Prerequisites check completed!"

# Setup Frontend
echo "🎨 Setting up Frontend..."
cd frontend

# Install dependencies
npm install

# Create environment file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "📝 Created frontend .env file. Please update REACT_APP_API_URL."
fi

echo "✅ Frontend setup completed!"

# Setup Backend
echo "🔧 Setting up Backend..."
cd ../backend

# Create virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
if [ ! -f .env ]; then
    cp .env.example .env
    echo "📝 Created backend .env file. Please update your API keys."
fi

echo "✅ Backend setup completed!"

# Return to root directory
cd ..

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📝 Next steps:"
echo "1. Update backend/.env with your OpenAI API key"
echo "2. Update frontend/.env with your API URL"
echo "3. Start the development servers:"
echo "   - Backend: cd backend && source venv/bin/activate && python main.py"
echo "   - Frontend: cd frontend && npm start"
echo ""
echo "🌐 The application will be available at:"
echo "   - Frontend: http://localhost:3000"
echo "   - Backend API: http://localhost:8000"
echo "   - API Docs: http://localhost:8000/api/docs"
echo ""
echo "📚 For more information, see README.md"
