import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowLeft, Users, Shield, BookOpen, Heart, Target, Award, Zap } from 'lucide-react';

const AboutPage: React.FC = () => {
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
              <Shield className="w-8 h-8 text-ai-purple-400" />
              <span className="text-2xl font-bold bg-gradient-to-r from-ai-purple-400 to-ai-purple-200 bg-clip-text text-transparent">
                Vani-Kanoon
              </span>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Hero Section */}
        <div className="text-center mb-16">
          <h1 className="text-5xl font-bold text-white mb-6">
            About <span className="bg-gradient-to-r from-ai-purple-400 to-ai-purple-200 bg-clip-text text-transparent">Vani-Kanoon</span>
          </h1>
          <p className="text-xl text-ai-purple-200 max-w-3xl mx-auto">
            Empowering rural India with AI-powered legal understanding and accessibility
          </p>
        </div>

        {/* Mission Section */}
        <div className="grid lg:grid-cols-2 gap-12 mb-16">
          <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-8">
            <div className="flex items-center mb-6">
              <Target className="w-8 h-8 text-ai-purple-400 mr-3" />
              <h2 className="text-3xl font-bold text-white">Our Mission</h2>
            </div>
            <p className="text-ai-purple-100 leading-relaxed mb-4">
              To bridge the justice gap in rural India by making legal documents accessible and understandable for everyone, regardless of their language proficiency or educational background.
            </p>
            <p className="text-ai-purple-200 leading-relaxed">
              We believe that access to justice is a fundamental right, and language should never be a barrier to understanding one's legal rights and obligations.
            </p>
          </div>

          <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-8">
            <div className="flex items-center mb-6">
              <Heart className="w-8 h-8 text-ai-purple-400 mr-3" />
              <h2 className="text-3xl font-bold text-white">Social Impact</h2>
            </div>
            <ul className="space-y-3">
              <li className="flex items-start">
                <Users className="w-5 h-5 text-ai-purple-300 mr-3 mt-1 flex-shrink-0" />
                <span className="text-ai-purple-100">Empowering 70% of rural population with limited English proficiency</span>
              </li>
              <li className="flex items-start">
                <Shield className="w-5 h-5 text-ai-purple-300 mr-3 mt-1 flex-shrink-0" />
                <span className="text-ai-purple-100">Protecting property rights and preventing exploitation</span>
              </li>
              <li className="flex items-start">
                <BookOpen className="w-5 h-5 text-ai-purple-300 mr-3 mt-1 flex-shrink-0" />
                <span className="text-ai-purple-100">Democratizing access to legal information</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Problem Section */}
        <div className="bg-gradient-to-r from-ai-purple-900/30 to-ai-purple-800/30 rounded-xl p-8 mb-16">
          <h2 className="text-3xl font-bold text-white mb-6 text-center">The Problem We're Solving</h2>
          <div className="grid md:grid-cols-3 gap-6">
            <div className="text-center">
              <div className="text-4xl font-bold text-ai-purple-400 mb-2">70%</div>
              <p className="text-ai-purple-200">Rural population has limited English proficiency</p>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-ai-purple-400 mb-2">90%</div>
              <p className="text-ai-purple-200">Legal documents are in complex English</p>
            </div>
            <div className="text-center">
              <div className="text-4xl font-bold text-ai-purple-400 mb-2">1:50,000</div>
              <p className="text-ai-purple-200">Lawyer-to-citizen ratio in rural areas</p>
            </div>
          </div>
        </div>

        {/* Technology Section */}
        <div className="mb-16">
          <h2 className="text-3xl font-bold text-white mb-8 text-center">Generative AI Technology</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6 text-center">
              <Zap className="w-12 h-12 text-ai-purple-400 mx-auto mb-4" />
              <h3 className="text-xl font-semibold text-white mb-2">OCR Technology</h3>
              <p className="text-ai-purple-200 text-sm">
                Advanced text extraction from scanned documents
              </p>
            </div>

            <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6 text-center">
              <BookOpen className="w-12 h-12 text-ai-purple-400 mx-auto mb-4" />
              <h3 className="text-xl font-semibold text-white mb-2">AI Simplification</h3>
              <p className="text-ai-purple-200 text-sm">
                Complex legal terms explained in simple language
              </p>
            </div>

            <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6 text-center">
              <Users className="w-12 h-12 text-ai-purple-400 mx-auto mb-4" />
              <h3 className="text-xl font-semibold text-white mb-2">Multi-language Support</h3>
              <p className="text-ai-purple-200 text-sm">
                Translation to 5 major regional languages
              </p>
            </div>

            <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6 text-center">
              <Target className="w-12 h-12 text-ai-purple-400 mx-auto mb-4" />
              <h3 className="text-xl font-semibold text-white mb-2">Interactive Q&A</h3>
              <p className="text-ai-purple-200 text-sm">
                AI-powered chatbot for follow-up questions
              </p>
            </div>
          </div>
        </div>

        {/* Features Section */}
        <div className="mb-16">
          <h2 className="text-3xl font-bold text-white mb-8 text-center">Key Features</h2>
          <div className="grid md:grid-cols-2 gap-6">
            <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6">
              <h3 className="text-xl font-semibold text-white mb-4">📄 Document Processing</h3>
              <ul className="space-y-2 text-ai-purple-200">
                <li>• PDF and image file support</li>
                <li>• High-accuracy OCR technology</li>
                <li>• Handwritten text recognition</li>
                <li>• Multiple document formats</li>
              </ul>
            </div>

            <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6">
              <h3 className="text-xl font-semibold text-white mb-4">🤖 AI Intelligence</h3>
              <ul className="space-y-2 text-ai-purple-200">
                <li>• Legal language simplification</li>
                <li>• Context-aware explanations</li>
                <li>• Rights and obligations identification</li>
                <li>• Risk assessment and warnings</li>
              </ul>
            </div>

            <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6">
              <h3 className="text-xl font-semibold text-white mb-4">🌍 Accessibility</h3>
              <ul className="space-y-2 text-ai-purple-200">
                <li>• 5 regional languages supported</li>
                <li>• Voice output for illiterate users</li>
                <li>• Low-bandwidth optimization</li>
                <li>• Mobile-friendly interface</li>
              </ul>
            </div>

            <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6">
              <h3 className="text-xl font-semibold text-white mb-4">💬 User Experience</h3>
              <ul className="space-y-2 text-ai-purple-200">
                <li>• Interactive chatbot assistance</li>
                <li>• Downloadable summaries</li>
                <li>• Simple, intuitive interface</li>
                <li>• Real-time processing</li>
              </ul>
            </div>
          </div>
        </div>

        {/* Recognition Section */}
        <div className="bg-gradient-to-r from-ai-purple-900/30 to-ai-purple-800/30 rounded-xl p-8 mb-16">
          <div className="flex items-center mb-6">
            <Award className="w-8 h-8 text-ai-purple-400 mr-3" />
            <h2 className="text-3xl font-bold text-white">Recognition & Support</h2>
          </div>
          <div className="grid md:grid-cols-3 gap-6 text-center">
            <div>
              <div className="text-2xl font-bold text-ai-purple-300 mb-2">🏆</div>
              <p className="text-ai-purple-200 font-semibold">Social Innovation Award</p>
              <p className="text-ai-purple-300 text-sm">Digital India Initiative</p>
            </div>
            <div>
              <div className="text-2xl font-bold text-ai-purple-300 mb-2">🤝</div>
              <p className="text-ai-purple-200 font-semibold">NGO Partnerships</p>
              <p className="text-ai-purple-300 text-sm">Rural Legal Aid Networks</p>
            </div>
            <div>
              <div className="text-2xl font-bold text-ai-purple-300 mb-2">📚</div>
              <p className="text-ai-purple-200 font-semibold">Academic Research</p>
              <p className="text-ai-purple-300 text-sm">Legal AI Studies</p>
            </div>
          </div>
        </div>

        {/* Call to Action */}
        <div className="text-center bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-8">
          <h2 className="text-3xl font-bold text-white mb-4">Join Our Mission</h2>
          <p className="text-ai-purple-200 mb-6 max-w-2xl mx-auto">
            Help us bring legal justice to every corner of rural India. Together, we can make a difference in millions of lives.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              to="/"
              className="inline-flex items-center px-8 py-3 bg-gradient-to-r from-ai-purple-600 to-ai-purple-500 text-white font-semibold rounded-lg hover:from-ai-purple-500 hover:to-ai-purple-400 transition-all transform hover:scale-105"
            >
              Try Vani-Kanoon
            </Link>
            <button className="inline-flex items-center px-8 py-3 bg-ai-dark-800 border border-ai-purple-600/50 text-ai-purple-200 font-semibold rounded-lg hover:bg-ai-dark-700 hover:border-ai-purple-500 transition-all">
              Partner With Us
            </button>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="bg-ai-dark-900/50 backdrop-blur-lg border-t border-ai-purple-800/20 py-12 mt-20">
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

export default AboutPage;
