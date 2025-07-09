# 🎤 Voice Assistant Web Application

A modern, Django-based voice assistant web application with real-time speech-to-text and text-to-speech capabilities, powered by LangChain, LangGraph, and Ollama for local AI processing.

## ✨ Features

### 🎯 Core Functionality
- **Voice Input/Output**: Real-time speech recognition and text-to-speech
- **AI Chat**: Intelligent conversations using local Ollama models
- **Conversation History**: Save and manage chat conversations
- **User Profiles**: Complete user management with profile pictures
- **Modern UI**: Responsive Bootstrap-based interface

### 🔐 User Management
- **User Registration & Authentication**: Secure login/logout system
- **Profile Management**: Upload profile pictures, edit personal info
- **Password Management**: Secure password change functionality
- **Session Management**: Proper session handling and security

### 💬 Chat Features
- **Real-time Chat**: Instant messaging with AI assistant
- **Voice Commands**: Speak to interact with the assistant
- **Text Input**: Type messages as an alternative to voice
- **Speaker Button**: Hear assistant responses aloud
- **Conversation Continuation**: Resume previous conversations
- **Message History**: View and manage past conversations

### 🎨 User Interface
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Professional Bootstrap styling
- **Profile Pictures**: User avatars throughout the interface
- **Intuitive Navigation**: Easy-to-use navigation system
- **Visual Feedback**: Loading states and status indicators

## 🛠️ Technology Stack

### Backend
- **Django 5.2+**: Web framework
- **SQLite**: Database (can be upgraded to PostgreSQL/MySQL)
- **LangChain**: AI framework integration
- **LangGraph**: Conversation flow management
- **Ollama**: Local AI model processing

### Frontend
- **Bootstrap 5.1.3**: UI framework
- **Font Awesome 6.0**: Icons
- **Web Speech API**: Browser-based speech recognition and synthesis
- **JavaScript**: Interactive functionality

### AI/ML
- **Ollama**: Local large language models
- **LangChain**: AI application framework
- **LangGraph**: Conversational AI workflows

## 📋 Prerequisites

- **Python 3.8+**
- **Ollama** installed and running locally
- **Modern web browser** with Web Speech API support
- **Git** (for cloning the repository)

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/cyberwithaman/voiceassistant.git
cd voiceassistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv

venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 🤖 Ollama Setup

### 1. Install Ollama
Visit [ollama.ai](https://ollama.ai) and follow the installation instructions for your platform.

### 2. Start Ollama Service
```bash
ollama serve
```

### 3. Pull AI Models
```bash
# Recommended models for different system specs
ollama pull llama2        # Good for most systems
ollama pull mistral       # Faster, smaller model
ollama pull codellama     # Good for coding tasks
ollama pull phi3          # Very fast, small model
```

### 4. Test Ollama Connection
```bash
python test_ollama_models.py
```

## 📁 Project Structure

```
voiceassistant/
├── assistant/                 # Main Django app
│   ├── migrations/           # Database migrations
│   ├── templates/           # HTML templates
│   ├── __init__.py
│   ├── admin.py            # Django admin configuration
│   ├── apps.py             # App configuration
│   ├── engine.py           # AI engine (Ollama integration)
│   ├── models.py           # Database models
│   ├── tests.py            # Unit tests
│   ├── urls.py             # URL routing
│   └── views.py            # View functions
├── voiceassistant/          # Django project settings
│   ├── __init__.py
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── templates/              # Global templates
│   ├── assistant/          # App-specific templates
│   ├── registration/       # Auth templates
│   └── base.html          # Base template
├── static/                # Static files
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   └── images/           # Images
├── media/                # User-uploaded files
├── logs/                 # Application logs
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🎮 Usage

### 1. User Registration
- Visit the application and click "Register"
- Fill in your details and create an account
- Upload a profile picture (optional)

### 2. Starting a Chat
- Click "Chat" in the navigation
- Use the microphone button for voice input
- Or type your message in the text field
- Click "Send" to get a response from the AI

### 3. Voice Commands
- Click the microphone icon to start voice recognition
- Speak clearly into your microphone
- The system will transcribe your speech to text
- Click the speaker button on assistant messages to hear responses

### 4. Managing Conversations
- View all conversations in "History"
- Continue previous conversations
- Delete conversations you no longer need

### 5. Profile Settings
- Click your username in the navigation
- Select "Settings" to manage your profile
- Update personal information, profile picture, and bio
- Change your password

## 🔧 Configuration
```

### AI Model Configuration
Edit `assistant/engine.py` to change:
- Model name (default: "llama2")
- Temperature and other generation parameters
- Response length limits
- Context window size

### Voice Settings
The application uses browser-based Web Speech API:
- **Speech Recognition**: Automatically uses system language settings
- **Text-to-Speech**: Automatically selects available voices
- **Voice Selection**: Prioritizes female voices when available

## 🐛 Troubleshooting

### Common Issues

#### 1. Ollama Connection Error
```
Error: Connection refused
```
**Solution**: Ensure Ollama is running:
```bash
ollama serve
```

#### 2. Voice Recognition Not Working
**Solution**: 
- Check microphone permissions in browser
- Ensure HTTPS in production (required for Web Speech API)
- Try a different browser (Chrome recommended)

#### 3. Text-to-Speech Not Working
**Solution**:
- Check browser console for errors
- Ensure system has available voices
- Try refreshing the page

#### 4. Database Migration Errors
**Solution**:
```bash
python manage.py makemigrations assistant
python manage.py migrate
```

#### 5. Static Files Not Loading
**Solution**:
```bash
python manage.py collectstatic
```

### Performance Optimization

#### For Better AI Response Speed:
1. Use smaller models (mistral, phi3)
2. Adjust generation parameters in `engine.py`
3. Reduce context window size
4. Use SSD storage for faster model loading

#### For Better Voice Recognition:
1. Use a high-quality microphone
2. Speak clearly and at normal volume
3. Minimize background noise
4. Use Chrome browser for best compatibility

## 🔒 Security Features

- **CSRF Protection**: All forms protected against CSRF attacks
- **Session Security**: Secure session management
- **Password Validation**: Django's built-in password strength validation
- **File Upload Security**: Secure profile picture uploads
- **SQL Injection Protection**: Django ORM protection
- **XSS Protection**: Template auto-escaping

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG=False` in settings
- [ ] Configure production database (PostgreSQL/MySQL)
- [ ] Set up static file serving (nginx/Apache)
- [ ] Configure HTTPS (required for Web Speech API)
- [ ] Set up proper logging
- [ ] Configure environment variables
- [ ] Set up backup system
- [ ] Configure monitoring

### Docker Deployment (Optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 🙏 Acknowledgments

- **Django**: Web framework
- **Bootstrap**: UI framework
- **Ollama**: Local AI models
- **LangChain**: AI application framework
- **Web Speech API**: Browser speech capabilities


**Made with ❤️ using Django, Bootstrap, and Ollama** 