import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Upload, FileText, Loader2, ArrowLeft, CheckCircle } from 'lucide-react';

const UploadPage: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [isUploading, setIsUploading] = useState(false);
  const [extractedText, setExtractedText] = useState('');
  const [uploadComplete, setUploadComplete] = useState(false);
  const navigate = useNavigate();

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile && (droppedFile.type === 'application/pdf' || droppedFile.type.startsWith('image/'))) {
      setFile(droppedFile);
    }
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  const handleUpload = async () => {
    if (!file) return;

    setIsUploading(true);
    
    // Simulate file upload and OCR processing
    setTimeout(() => {
      // Mock extracted text
      const mockText = `This Agreement is made and entered into on this 1st day of January, 2024, between Party A and Party B. 
      
      WHEREAS, Party A is the owner of the property situated at Rural Village, District, and Party B wishes to purchase the said property;
      
      WHEREAS, the parties have agreed to the terms and conditions set forth herein;
      
      NOW, THEREFORE, in consideration of the mutual covenants contained herein, the parties agree as follows:
      
      1. Party A agrees to sell and Party B agrees to purchase the property for a total consideration of ₹5,00,000.
      2. Party B shall pay 20% of the consideration as advance payment.
      3. The sale shall be completed within 90 days from the date of this agreement.
      4. Party A warrants that they have clear title to the property.
      5. This agreement shall be governed by the laws of India.`;
      
      setExtractedText(mockText);
      setIsUploading(false);
      setUploadComplete(true);
    }, 3000);
  };

  const handleSimplifyAndTranslate = () => {
    // Navigate to result page with extracted text
    navigate('/result', { state: { extractedText } });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-ai-dark-950 via-ai-purple-900 to-ai-dark-950">
      {/* Navigation */}
      <nav className="bg-ai-dark-900/50 backdrop-blur-lg border-b border-ai-purple-800/20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-2">
              <Link to="/" className="flex items-center space-x-2 text-ai-purple-200 hover:text-ai-purple-100 transition-colors">
                <ArrowLeft className="w-5 h-5" />
                <span>Back to Home</span>
              </Link>
            </div>
            <div className="flex items-center space-x-2">
              <FileText className="w-8 h-8 text-ai-purple-400" />
              <span className="text-2xl font-bold bg-gradient-to-r from-ai-purple-400 to-ai-purple-200 bg-clip-text text-transparent">
                Vani-Kanoon
              </span>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <h1 className="text-4xl font-bold text-center text-white mb-8">
          Upload Legal Document
        </h1>

        {!uploadComplete ? (
          <div className="space-y-8">
            {/* Upload Area */}
            <div
              className={`relative border-2 border-dashed rounded-xl p-12 text-center transition-all
                ${isDragging 
                  ? 'border-ai-purple-400 bg-ai-purple-900/20' 
                  : 'border-ai-purple-600/50 bg-ai-dark-900/50'
                } hover:border-ai-purple-400 hover:bg-ai-purple-900/20`}
              onDragOver={handleDragOver}
              onDragLeave={handleDragLeave}
              onDrop={handleDrop}
            >
              <input
                type="file"
                accept=".pdf,image/*"
                onChange={handleFileSelect}
                className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                disabled={isUploading}
              />
              
              <div className="flex flex-col items-center space-y-4">
                <Upload className="w-16 h-16 text-ai-purple-400" />
                <div>
                  <p className="text-xl text-white mb-2">
                    {file ? file.name : 'Drop your document here or click to browse'}
                  </p>
                  <p className="text-ai-purple-200">
                    Supports PDF and image files (JPG, PNG)
                  </p>
                </div>
              </div>
            </div>

            {/* Upload Button */}
            {file && (
              <div className="text-center">
                <button
                  onClick={handleUpload}
                  disabled={isUploading}
                  className="inline-flex items-center px-8 py-4 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 text-white font-semibold rounded-lg hover:from-ai-purple-500 hover:to-ai-purple-400 transition-all transform hover:scale-105 shadow-lg hover:shadow-ai-purple-500/25 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {isUploading ? (
                    <>
                      <Loader2 className="w-5 h-5 mr-2 animate-spin" />
                      Processing Document...
                    </>
                  ) : (
                    <>
                      <Upload className="w-5 h-5 mr-2" />
                      Upload & Extract Text
                    </>
                  )}
                </button>
              </div>
            )}

            {/* Processing Status */}
            {isUploading && (
              <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6">
                <div className="flex items-center space-x-3">
                  <Loader2 className="w-6 h-6 text-ai-purple-400 animate-spin" />
                  <div>
                    <p className="text-white font-semibold">Processing your document...</p>
                    <p className="text-ai-purple-200 text-sm">
                      Extracting text using OCR technology
                    </p>
                  </div>
                </div>
              </div>
            )}
          </div>
        ) : (
          <div className="space-y-8">
            {/* Success Message */}
            <div className="bg-green-900/20 border border-green-600/30 rounded-xl p-6">
              <div className="flex items-center space-x-3">
                <CheckCircle className="w-6 h-6 text-green-400" />
                <div>
                  <p className="text-white font-semibold">Document processed successfully!</p>
                  <p className="text-green-200 text-sm">
                    Text has been extracted from your document
                  </p>
                </div>
              </div>
            </div>

            {/* Extracted Text */}
            <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6">
              <h3 className="text-xl font-semibold text-white mb-4">Extracted Text</h3>
              <div className="bg-ai-dark-800/50 rounded-lg p-4 max-h-96 overflow-y-auto">
                <p className="text-ai-purple-100 whitespace-pre-wrap leading-relaxed">
                  {extractedText}
                </p>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="flex flex-col sm:flex-row gap-4">
              <button
                onClick={handleSimplifyAndTranslate}
                className="flex-1 inline-flex items-center justify-center px-8 py-4 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 text-white font-semibold rounded-lg hover:from-ai-purple-500 hover:to-ai-purple-400 transition-all transform hover:scale-105 shadow-lg hover:shadow-ai-purple-500/25"
              >
                Simplify & Translate
              </button>
              
              <button
                onClick={() => {
                  setFile(null);
                  setExtractedText('');
                  setUploadComplete(false);
                }}
                className="flex-1 inline-flex items-center justify-center px-8 py-4 bg-ai-dark-800 border border-ai-purple-600/50 text-ai-purple-200 font-semibold rounded-lg hover:bg-ai-dark-700 hover:border-ai-purple-500 transition-all"
              >
                Upload Another Document
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default UploadPage;
