import React, { useState, useEffect } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { ArrowLeft, MessageCircle, Volume2, Download, Loader2, Globe, BookOpen } from 'lucide-react';

interface ResultState {
  extractedText: string;
}

const ResultPage: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const state = location.state as ResultState;
  
  const [simplifiedText, setSimplifiedText] = useState('');
  const [translatedText, setTranslatedText] = useState('');
  const [selectedLanguage, setSelectedLanguage] = useState('kannada');
  const [isProcessing, setIsProcessing] = useState(true);
  const [chatMessages, setChatMessages] = useState<Array<{ role: string; content: string }>>([]);
  const [currentMessage, setCurrentMessage] = useState('');
  const [isChatLoading, setIsChatLoading] = useState(false);

  const languages = [
    { code: 'kannada', name: 'Kannada', nativeName: 'ಕನ್ನಡ' },
    { code: 'hindi', name: 'Hindi', nativeName: 'हिंदी' },
    { code: 'marathi', name: 'Marathi', nativeName: 'मराठी' },
    { code: 'tamil', name: 'Tamil', nativeName: 'தமிழ்' },
    { code: 'telugu', name: 'Telugu', nativeName: 'తెలుగు' },
  ];

  useEffect(() => {
    if (!state?.extractedText) {
      navigate('/upload');
      return;
    }

    // Simulate AI processing
    setTimeout(() => {
      // Mock simplified text
      setSimplifiedText(`This is a simple property sale agreement made on January 1, 2024, between two parties.

**What this means:**
- Party A owns a property in a rural village
- Party B wants to buy this property for ₹5,00,000 (5 lakh rupees)
- Party B must pay 20% (₹1,00,000) as advance payment
- The sale must be completed within 90 days
- Party A guarantees they legally own the property

**Your Rights:**
- As the buyer, you have the right to clear property ownership
- You have 90 days to complete the purchase
- The seller must have proper legal documents

**Important Points:**
- Make sure to verify all property documents
- Keep records of all payments
- Consider getting legal advice before signing

**What to Watch For:**
- Hidden fees or additional costs
- Property boundary disputes
- Any existing loans on the property`);

      // Mock translated text
      setTranslatedText(`ಇದು ಜನವರಿ 1, 2024 ರಂದು ಎರಡು ಪಕ್ಷಗಳ ನಡುವೆ ಮಾಡಿಕೊಂಡ ಸರಳ ಆಸ್ತಿ ಮಾರಾಟ ಒಪ್ಪಂದವಾಗಿದೆ.

**ಇದರ ಅರ್ಥ ಏನು:**
- ಪಕ್ಷ A ಗ್ರಾಮೀಣ ಹಳ್ಳಿಯಲ್ಲಿ ಆಸ್ತಿಯನ್ನು ಹೊಂದಿದ್ದಾರೆ
- ಪಕ್ಷ B ಈ ಆಸ್ತಿಯನ್ನು ₹5,00,000 (ಐದು ಲಕ್ಷ ರೂಪಾಯಿಗಳಿಗೆ) ಖರೀದಿಸಲು ಬಯಸುತ್ತಾರೆ
- ಪಕ್ಷ B 20% (₹1,00,000) ಅಗ್ರಿಮ ಪಾವತಿಯಾಗಿ ಪಾವತಿಸಬೇಕು
- ಮಾರಾಟವನ್ನು 90 ದಿನಗಳೊಳಗೆ ಪೂರ್ಣಗೊಳಿಸಬೇಕು
- ಪಕ್ಷ A ಅವರು ಕಾನೂನುಬದ್ಧವಾಗಿ ಆಸ್ತಿಯನ್ನು ಹೊಂದಿದ್ದಾರೆ ಎಂದು ಖಾತರಿಪಡಿಸುತ್ತಾರೆ

**ನಿಮ್ಮ ಹಕ್ಕುಗಳು:**
- ಖರೀದಿದಾರರಾಗಿ, ನಿಮಗೆ ಸ್ಪಷ್ಟ ಆಸ್ತಿ ಮಾಲೀಕತ್ವದ ಹಕ್ಕು ಇದೆ
- ಖರೀದಿಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು ನಿಮಗೆ 90 ದಿನಗಳು ಇವೆ
- ಮಾರಾಟಗಾರರು ಸರಿಯಾದ ಕಾನೂನು ದಾಖಲೆಗಳನ್ನು ಹೊಂದಿರಬೇಕು

**ಪ್ರಮುಖ ಅಂಶಗಳು:**
- ಎಲ್ಲಾ ಆಸ್ತಿ ದಾಖಲೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ
- ಎಲ್ಲಾ ಪಾವತಿಗಳ ದಾಖಲೆಗಳನ್ನು ಇರಿಸಿಕೊಳ್ಳಿ
- ಸಹಿ ಮಾಡುವ ಮೊದಲು ಕಾನೂನು ಸಲಹೆ ಪಡೆಯಿರಿ ಪರಿಗಣಿಸಿ

**ಗಮನಿಸಬೇಕಾದ ವಿಷಯಗಳು:**
- ಮರೆಮಾಚಿದ ಶುಲ್ಕಗಳು ಅಥವಾ ಹೆಚ್ಚುವರಿ ವೆಚ್ಚಗಳು
- ಆಸ್ತಿ ಗಡಿ ವಿವಾದಗಳು
- ಆಸ್ತಿಯ ಮೇಲೆ ಯಾವುದೇ ಸಾಲಗಳು ಇರುವುದು`);

      setIsProcessing(false);
    }, 3000);
  }, [state, navigate]);

  const handleLanguageChange = (languageCode: string) => {
    setSelectedLanguage(languageCode);
    // Simulate translation
    setIsProcessing(true);
    setTimeout(() => {
      // In real app, this would call translation API
      setTranslatedText(`Translation in ${languageCode} would appear here...`);
      setIsProcessing(false);
    }, 1500);
  };

  const handleSendMessage = async () => {
    if (!currentMessage.trim()) return;

    const userMessage = currentMessage;
    setCurrentMessage('');
    setIsChatLoading(true);

    // Add user message
    setChatMessages(prev => [...prev, { role: 'user', content: userMessage }]);

    // Simulate AI response
    setTimeout(() => {
      const aiResponse = `Based on the document, ${userMessage.toLowerCase().includes('rights') 
        ? 'you have the right to clear property ownership and proper documentation. The seller must provide all legal papers and clear title.'
        : userMessage.toLowerCase().includes('safe')
        ? 'this agreement appears standard for property sales. However, I recommend verifying all property documents and getting legal advice before signing.'
        : userMessage.toLowerCase().includes('mean')
        ? 'this is a property sale agreement where Party A is selling rural property to Party B for ₹5,00,000 with 20% advance payment.'
        : 'that\'s a good question about the document. Let me explain that this agreement outlines the terms for purchasing rural property with specific payment terms and timeline.'
      }`;
      
      setChatMessages(prev => [...prev, { role: 'assistant', content: aiResponse }]);
      setIsChatLoading(false);
    }, 2000);
  };

  const handleVoiceOutput = () => {
    // Simulate text-to-speech
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(simplifiedText);
      utterance.lang = 'en-US';
      speechSynthesis.speak(utterance);
    }
  };

  const handleDownloadPDF = () => {
    // Simulate PDF download
    const content = `Simplified Legal Explanation\n\n${simplifiedText}\n\nTranslation (${selectedLanguage}):\n${translatedText}`;
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'legal-document-explanation.txt';
    a.click();
    URL.revokeObjectURL(url);
  };

  if (!state?.extractedText) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-ai-dark-950 via-ai-purple-900 to-ai-dark-950">
      {/* Navigation */}
      <nav className="bg-ai-dark-900/50 backdrop-blur-lg border-b border-ai-purple-800/20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-2">
              <Link to="/upload" className="flex items-center space-x-2 text-ai-purple-200 hover:text-ai-purple-100 transition-colors">
                <ArrowLeft className="w-5 h-5" />
                <span>Back to Upload</span>
              </Link>
            </div>
            <div className="flex items-center space-x-2">
              <BookOpen className="w-8 h-8 text-ai-purple-400" />
              <span className="text-2xl font-bold bg-gradient-to-r from-ai-purple-400 to-ai-purple-200 bg-clip-text text-transparent">
                Vani-Kanoon
              </span>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <h1 className="text-4xl font-bold text-center text-white mb-8">
          AI Legal Analysis
        </h1>

        {isProcessing ? (
          <div className="flex flex-col items-center justify-center py-20">
            <Loader2 className="w-16 h-16 text-ai-purple-400 animate-spin mb-4" />
            <p className="text-xl text-ai-purple-200">AI is analyzing your document...</p>
            <p className="text-ai-purple-300 mt-2">Simplifying legal language and translating to your language</p>
          </div>
        ) : (
          <div className="grid lg:grid-cols-2 gap-8">
            {/* Simplified Explanation */}
            <div className="space-y-6">
              <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6">
                <div className="flex items-center justify-between mb-4">
                  <h2 className="text-2xl font-semibold text-white">Simplified Explanation</h2>
                  <div className="flex space-x-2">
                    <button
                      onClick={handleVoiceOutput}
                      className="p-2 bg-ai-purple-600/20 text-ai-purple-300 rounded-lg hover:bg-ai-purple-600/30 transition-colors"
                      title="Listen to explanation"
                    >
                      <Volume2 className="w-5 h-5" />
                    </button>
                    <button
                      onClick={handleDownloadPDF}
                      className="p-2 bg-ai-purple-600/20 text-ai-purple-300 rounded-lg hover:bg-ai-purple-600/30 transition-colors"
                      title="Download explanation"
                    >
                      <Download className="w-5 h-5" />
                    </button>
                  </div>
                </div>
                <div className="bg-ai-dark-800/50 rounded-lg p-4 max-h-96 overflow-y-auto">
                  <div className="text-ai-purple-100 whitespace-pre-wrap leading-relaxed">
                    {simplifiedText.split('\n').map((line, index) => (
                      <div key={index} className="mb-2">
                        {line.startsWith('**') ? (
                          <p className="font-semibold text-ai-purple-200">{line.replace(/\*\*/g, '')}</p>
                        ) : line.startsWith('-') ? (
                          <p className="ml-4 text-ai-purple-100">• {line.substring(1).trim()}</p>
                        ) : (
                          <p>{line}</p>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* Language Selection */}
              <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6">
                <div className="flex items-center mb-4">
                  <Globe className="w-6 h-6 text-ai-purple-400 mr-2" />
                  <h2 className="text-xl font-semibold text-white">Select Language</h2>
                </div>
                <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
                  {languages.map((lang) => (
                    <button
                      key={lang.code}
                      onClick={() => handleLanguageChange(lang.code)}
                      className={`px-4 py-2 rounded-lg font-medium transition-all
                        ${selectedLanguage === lang.code
                          ? 'bg-ai-purple-600 text-white'
                          : 'bg-ai-dark-800 text-ai-purple-200 hover:bg-ai-dark-700'
                        }`}
                    >
                      <div className="text-sm">{lang.nativeName}</div>
                      <div className="text-xs opacity-75">{lang.name}</div>
                    </button>
                  ))}
                </div>
              </div>
            </div>

            {/* Translation and Chat */}
            <div className="space-y-6">
              {/* Translated Text */}
              <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6">
                <h2 className="text-2xl font-semibold text-white mb-4">
                  Translation ({languages.find(l => l.code === selectedLanguage)?.nativeName})
                </h2>
                <div className="bg-ai-dark-800/50 rounded-lg p-4 max-h-64 overflow-y-auto">
                  <p className="text-ai-purple-100 whitespace-pre-wrap leading-relaxed">
                    {translatedText}
                  </p>
                </div>
              </div>

              {/* Chat Interface */}
              <div className="bg-ai-dark-900/50 backdrop-blur-lg border border-ai-purple-800/20 rounded-xl p-6">
                <div className="flex items-center mb-4">
                  <MessageCircle className="w-6 h-6 text-ai-purple-400 mr-2" />
                  <h2 className="text-xl font-semibold text-white">Ask Questions</h2>
                </div>
                
                <div className="bg-ai-dark-800/50 rounded-lg p-4 h-64 overflow-y-auto mb-4">
                  {chatMessages.length === 0 ? (
                    <p className="text-ai-purple-300 text-center">
                      Ask me anything about your legal document...
                    </p>
                  ) : (
                    <div className="space-y-3">
                      {chatMessages.map((message, index) => (
                        <div
                          key={index}
                          className={`p-3 rounded-lg ${
                            message.role === 'user'
                              ? 'bg-ai-purple-600/20 ml-8'
                              : 'bg-ai-dark-700/50 mr-8'
                          }`}
                        >
                          <p className={`text-sm ${
                            message.role === 'user' ? 'text-ai-purple-200' : 'text-ai-purple-100'
                          }`}>
                            {message.content}
                          </p>
                        </div>
                      ))}
                      {isChatLoading && (
                        <div className="flex items-center space-x-2 text-ai-purple-300">
                          <Loader2 className="w-4 h-4 animate-spin" />
                          <p className="text-sm">AI is thinking...</p>
                        </div>
                      )}
                    </div>
                  )}
                </div>

                <div className="flex space-x-2">
                  <input
                    type="text"
                    value={currentMessage}
                    onChange={(e) => setCurrentMessage(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                    placeholder="What does this agreement mean?"
                    className="flex-1 px-4 py-2 bg-ai-dark-800 border border-ai-purple-600/30 rounded-lg text-ai-purple-100 placeholder-ai-purple-400 focus:outline-none focus:border-ai-purple-500"
                    disabled={isChatLoading}
                  />
                  <button
                    onClick={handleSendMessage}
                    disabled={isChatLoading || !currentMessage.trim()}
                    className="px-4 py-2 bg-ai-purple-600 text-white rounded-lg hover:bg-ai-purple-500 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    Send
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ResultPage;
