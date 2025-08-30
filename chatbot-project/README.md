# AI Chatbot - English Conversation Assistant

A modern, responsive web-based chatbot built with Python Flask. Available in two versions: **Hardcoded** (predefined responses) and **OpenAI-powered** (intelligent AI responses).

## 🚀 Two Versions Available

### **Version 1: Hardcoded Chatbot (`app.py`)**
- ✅ **No API key required**
- ✅ **Works offline**
- ✅ **Fast responses**
- ✅ **Predictable behavior**
- 📝 Uses predefined conversation patterns

### **Version 2: OpenAI Chatbot (`appOAI.py`)**
- 🤖 **AI-powered intelligent responses**
- 🌍 **Handles any topic or language**
- 🎯 **Context-aware conversations**
- ⚡ **Dynamic and engaging**
- 🔑 Requires OpenAI API key

## Features

- 💬 **Real-time Chat**: Instant message exchange with typing indicators
- 🎨 **Modern UI**: Beautiful, responsive design with gradient backgrounds
- 📱 **Mobile Friendly**: Works perfectly on all device sizes
- ⚡ **Fast & Lightweight**: Built with Flask for optimal performance
- 🎯 **Smart Suggestions**: Quick response chips for common phrases
- 🔧 **Easy Configuration**: Simple setup for both versions
- 🛡️ **Fallback System**: Graceful handling when API is unavailable (OpenAI version)

## Quick Start

### **Option 1: Hardcoded Version (Recommended for beginners)**
```bash
# Double-click this file or run:
run_chatbot_hardcoded.bat

# Or manually:
python app.py
```

### **Option 2: OpenAI Version (Requires API key)**
```bash
# First, set up your OpenAI API key:
python setup_openai.py

# Then run:
run_chatbot_openai.bat

# Or manually:
python appOAI.py
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- OpenAI API key (only for OpenAI version)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Choose Your Version

#### **For Hardcoded Version:**
No additional setup required! Just run:
```bash
python app.py
```

#### **For OpenAI Version:**
1. Get an OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Run the setup script:
   ```bash
   python setup_openai.py
   ```
3. Start the chatbot:
   ```bash
   python appOAI.py
   ```

### Step 3: Access the Chatbot
Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
chatbot-project/
├── app.py                    # Hardcoded version (no API key needed)
├── appOAI.py                 # OpenAI version (requires API key)
├── config.py                 # Configuration settings for OpenAI
├── setup_openai.py           # OpenAI API setup script
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── run_chatbot_hardcoded.bat # Easy start for hardcoded version
├── run_chatbot_openai.bat    # Easy start for OpenAI version
├── test_chatbot.py          # Test script for hardcoded version
└── templates/
    └── index.html           # Web interface template
```

## Conversation Data (Hardcoded Version)

The hardcoded version includes predefined patterns for:
- **Greetings**: "hello", "hi", "hey", "good morning", etc.
- **Farewells**: "bye", "goodbye", "see you", etc.
- **Well-being**: "how are you", "how are you doing", etc.
- **Gratitude**: "thank you", "thanks", etc.
- **Weather**: "weather", "temperature", "hot", "cold", etc.

## API Endpoints

### Hardcoded Version (`app.py`)
- `GET /` - Main chat interface
- `POST /chat` - Send message and get hardcoded response
- `GET /api/conversation-data` - Get conversation patterns

### OpenAI Version (`appOAI.py`)
- `GET /` - Main chat interface
- `POST /chat` - Send message and get AI response
- `GET /api/health` - Check OpenAI connection status

## Configuration

### OpenAI Settings (config.py)
- **Model**: `gpt-3.5-turbo` (can be changed to `gpt-4`)
- **Max Tokens**: 150 (response length limit)
- **Temperature**: 0.7 (creativity level)
- **System Prompt**: Defines chatbot personality and behavior

## Usage

1. **Start a Conversation**: Type your message in the input field
2. **Quick Responses**: Click on suggestion chips for common phrases
3. **Send Messages**: Press Enter or click the Send button
4. **Real-time Chat**: Watch the bot respond with intelligent replies

## Comparison

| Feature | Hardcoded Version | OpenAI Version |
|---------|------------------|----------------|
| **Setup** | No API key needed | Requires OpenAI API key |
| **Cost** | Free | Pay per usage |
| **Speed** | Instant | 1-3 seconds |
| **Intelligence** | Basic patterns | Advanced AI |
| **Offline** | ✅ Yes | ❌ No |
| **Customization** | Edit code | Change prompts |
| **Topics** | Limited | Unlimited |

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   - Change the port in the respective app file
   - Or kill existing processes: `taskkill /f /im python.exe`

2. **OpenAI API Key Not Configured**
   - Run: `python setup_openai.py`
   - Or manually edit `config.py`

3. **Dependencies Not Found**
   - Run: `pip install -r requirements.txt`

4. **Browser Not Loading**
   - Check if the server is running
   - Try accessing `http://127.0.0.1:5000`

## Cost Considerations (OpenAI Version)

- OpenAI API usage incurs costs based on token usage
- GPT-3.5-turbo is more cost-effective than GPT-4
- Monitor your usage at [OpenAI Usage Dashboard](https://platform.openai.com/usage)

## Contributing

Feel free to enhance either version by:
- Adding more conversation patterns (hardcoded)
- Improving the UI/UX
- Adding conversation memory/history
- Implementing user authentication
- Adding voice input/output

## License

This project is open source and available under the MIT License.

---

**Choose your version and start chatting! 🤖✨**
