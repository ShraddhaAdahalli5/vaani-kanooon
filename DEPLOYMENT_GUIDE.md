# 🚀 Vani-Kanoon Deployment Guide

This guide will help you deploy Vani-Kanoon to make it publicly accessible on the internet.

## 📋 Prerequisites

Before deploying, make sure you have:
- GitHub repository with the project code
- OpenAI API key
- (Optional) Google Cloud Translation API key
- Accounts on Vercel and Render

## 🗂️ Project Structure

```
vani-kanoon/
├── frontend/          # React frontend (deploys to Vercel)
├── backend/           # FastAPI backend (deploys to Render)
├── DEPLOYMENT_GUIDE.md
└── README.md
```

## 🔧 Configuration Status

### ✅ Frontend Configuration
- **Vercel config**: `frontend/vercel.json` ✅
- **Build scripts**: `package.json` ✅
- **API URL**: Configured for production backend ✅
- **Build test**: Passing ✅

### ✅ Backend Configuration
- **Render config**: `backend/render.yaml` ✅
- **Port**: Set to 10000 for Render ✅
- **CORS**: Configured for production domains ✅
- **Environment**: Production ready ✅

## 🌐 Deployment Steps

### Step 1: Deploy Backend to Render

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the `vani-kanoon` repository
   - Configure as follows:

   ```yaml
   Name: vani-kanoon-api
   Environment: Python 3
   Root Directory: backend
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

3. **Set Environment Variables**
   ```
   PORT=10000
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_TRANSLATE_API_KEY=your_google_translate_key_here (optional)
   DEBUG=false
   API_HOST=0.0.0.0
   API_PORT=10000
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Note the deployed URL: `https://vani-kanoon-api.onrender.com`

### Step 2: Deploy Frontend to Vercel

1. **Create Vercel Account**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with GitHub

2. **Import Project**
   - Click "New Project"
   - Select the `vani-kanoon` repository
   - Configure as follows:

   ```json
   {
     "Framework": "Create React App",
     "Root Directory": "frontend",
     "Build Command": "npm run build",
     "Output Directory": "build"
   }
   ```

3. **Set Environment Variables**
   ```
   REACT_APP_API_URL=https://vani-kanoon-api.onrender.com
   ```

4. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete
   - Note the deployed URL: `https://vani-kanoon.vercel.app`

## 🔍 Testing the Deployment

### Backend API Tests
```bash
# Health check
curl https://vani-kanoon-api.onrender.com/api/health

# API documentation
# Visit: https://vani-kanoon-api.onrender.com/api/docs

# Supported languages
curl https://vani-kanoon-api.onrender.com/api/languages/
```

### Frontend Tests
- Visit: `https://vani-kanoon.vercel.app`
- Test document upload
- Test AI simplification
- Test language translation
- Test chat functionality

## 🛠️ Troubleshooting

### Common Issues

#### 1. CORS Errors
**Problem**: Frontend can't connect to backend
**Solution**: Ensure backend CORS includes your frontend URL
```python
# In backend/app/config.py
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://vani-kanoon.vercel.app"
]
```

#### 2. API Connection Issues
**Problem**: API calls fail
**Solution**: Check environment variables
```bash
# Frontend .env
REACT_APP_API_URL=https://vani-kanoon-api.onrender.com

# Backend environment variables
OPENAI_API_KEY=your_key_here
```

#### 3. Build Failures
**Problem**: Frontend build fails
**Solution**: Check dependencies and build scripts
```bash
cd frontend
npm install
npm run build
```

#### 4. Backend Deployment Issues
**Problem**: Backend fails to start
**Solution**: Check Python dependencies and port configuration
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 10000
```

## 📊 Monitoring

### Backend Health
- URL: `https://vani-kanoon-api.onrender.com/api/health`
- Expected response:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "services": {
    "ocr": "active",
    "ai": "active",
    "translation": "active"
  }
}
```

### Frontend Performance
- Use Vercel Analytics
- Check Core Web Vitals
- Monitor API response times

## 🔄 Updating the Application

### Backend Updates
1. Push changes to GitHub
2. Render auto-deploys from main branch
3. Monitor deployment logs

### Frontend Updates
1. Push changes to GitHub
2. Vercel auto-deploys from main branch
3. Preview deployments available for PRs

## 💡 Best Practices

1. **Environment Variables**: Never commit API keys
2. **Error Handling**: Implement proper error boundaries
3. **Monitoring**: Set up alerts for failures
4. **Security**: Use HTTPS and validate inputs
5. **Performance**: Optimize images and API calls

## 🎉 Success Criteria

Your deployment is successful when:
- ✅ Backend health check passes
- ✅ Frontend loads without errors
- ✅ Document upload works
- ✅ AI processing functions
- ✅ Translation works
- ✅ Chat interface responds

## 📞 Support

If you encounter issues:
1. Check deployment logs
2. Verify environment variables
3. Test API endpoints directly
4. Review this troubleshooting guide

---

**Ready to go live! 🚀**
