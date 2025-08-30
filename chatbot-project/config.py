"""
Configuration file for the AI Chatbot
Set your OpenAI API key here or use environment variables
"""

import os

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OpenAI Model Settings
OPENAI_MODEL = "gpt-3.5-turbo"  # You can change to "gpt-4" if you have access
MAX_TOKENS = 150
TEMPERATURE = 0.7
PRESENCE_PENALTY = 0.1
FREQUENCY_PENALTY = 0.1

# Flask Configuration
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = True

# System Prompt for the chatbot
SYSTEM_PROMPT = """You are a friendly and helpful AI conversation assistant. You should:
- Be conversational and engaging
- Provide helpful and informative responses
- Keep responses concise but friendly
- Ask follow-up questions to keep the conversation flowing
- Be polite and respectful
- Respond in a natural, human-like way
- If you don't know something, be honest about it
- Focus on English conversation and language learning if relevant
- Keep responses under 150 words for better conversation flow"""
