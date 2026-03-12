import React from 'react';
import { Link } from 'react-router-dom';
import { Upload, BookOpen, MessageCircle, Shield, ArrowRight, Volume2 } from 'lucide-react';

const HomePage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-ai-dark-950 via-ai-purple-900 to-ai-dark-950">
      {/* Navigation */}
      <nav className="bg-ai-dark-900/50 backdrop-blur-lg border-b border-ai-purple-800/20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-2">
              <Shield className="w-8 h-8 text-ai-purple-400" />
              <span className="text-2xl font-bold bg-gradient-to-r from-ai-purple-400 to-ai-purple-200 bg-clip-text text-transparent">
                Vani-Kanoon
              </span>
            </div>
            <div className="flex space-x-6">
              <Link to="/" className="text-ai-purple-200 hover:text-ai-purple-100 transition-colors">
                Home
              </Link>
              <Link to="/about" className="text-ai-purple-200 hover:text-ai-purple-100 transition-colors">
                About
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <div className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-ai-purple-800/20 to-ai-purple-600/20"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
          <div className="text-center">
            <h1 className="text-5xl md:text-7xl font-bold text-white mb-6">
              <span className="bg-gradient-to-r from-ai-purple-400 via-ai-purple-300 to-ai-purple-200 bg-clip-text text-transparent">
                Vani-Kanoon
              </span>
              <br />
              <span className="text-3xl md:text-4xl text-ai-purple-200">The Legal Bridge</span>
            </h1>
            <p className="text-xl md:text-2xl text-ai-purple-100 mb-8 max-w-3xl mx-auto">
              AI-powered legal understanding for rural India
            </p>
            <p className="text-lg text-ai-purple-200 mb-12 max-w-2xl mx-auto">
              Transform complex legal documents into simple, understandable explanations in your regional language
            </p>
            
            <Link
              to="/upload"
              className="inline-flex items-center px-8 py-4 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 text-white font-semibold rounded-lg hover:from-ai-purple-500 hover:to-ai-purple-400 transition-all transform hover:scale-105 shadow-lg hover:shadow-ai-purple-500/25"
            >
              <Upload className="w-5 h-5 mr-2" />
              Upload Document
              <ArrowRight className="w-5 h-5 ml-2" />
            </Link>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <h2 className="text-4xl font-bold text-center text-white mb-16">
          How We Help You
        </h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6 hover:border-ai-purple-600/40 transition-all">
            <div className="w-12 h-12 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 rounded-lg flex items-center justify-center mb-4">
              <Upload className="w-6 h-6 text-white" />
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">Easy Upload</h3>
            <p className="text-ai-purple-200">
              Upload PDF or image documents with a simple click
            </p>
          </div>

          <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6 hover:border-ai-purple-600/40 transition-all">
            <div className="w-12 h-12 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 rounded-lg flex items-center justify-center mb-4">
              <BookOpen className="w-6 h-6 text-white" />
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">AI Simplification</h3>
            <p className="text-ai-purple-200">
              Complex legal terms explained in simple language
            </p>
          </div>

          <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6 hover:border-ai-purple-600/40 transition-all">
            <div className="w-12 h-12 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 rounded-lg flex items-center justify-center mb-4">
              <Volume2 className="w-6 h-6 text-white" />
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">Regional Languages</h3>
            <p className="text-ai-purple-200">
              Available in Kannada, Hindi, Marathi, Tamil, and Telugu
            </p>
          </div>

          <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6 hover:border-ai-purple-600/40 transition-all">
            <div className="w-12 h-12 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 rounded-lg flex items-center justify-center mb-4">
              <MessageCircle className="w-6 h-6 text-white" />
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">Ask Questions</h3>
            <p className="text-ai-purple-200">
              Get answers about your legal documents instantly
            </p>
          </div>
        </div>
      </div>

      {/* How It Works */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <h2 className="text-4xl font-bold text-center text-white mb-16">
          How It Works
        </h2>
        <div className="grid md:grid-cols-3 gap-8">
          <div className="text-center">
            <div className="w-16 h-16 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl font-bold text-white">1</span>
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">Upload Document</h3>
            <p className="text-ai-purple-200">
              Upload your legal document in PDF or image format
            </p>
          </div>

          <div className="text-center">
            <div className="w-16 h-16 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl font-bold text-white">2</span>
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">AI Processing</h3>
            <p className="text-ai-purple-200">
              Our AI extracts text and simplifies legal language
            </p>
          </div>

          <div className="text-center">
            <div className="w-16 h-16 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl font-bold text-white">3</span>
            </div>
            <h3 className="text-xl font-semibold text-white mb-2">Get Results</h3>
            <p className="text-ai-purple-200">
              Receive simplified explanations in your language
            </p>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="bg-ai-dark-900/50 backdrop-blur-lg border-t border-ai-purple-800/20 py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-ai-purple-200">
            Empowering rural India with accessible legal understanding
          </p>
          <p className="text-ai-purple-300 mt-2">
            Made with ❤️ for social impact
          </p>
        </div>
      </footer>
    </div>
  );
};

export default HomePage;
