from flask import Flask, render_template, request, jsonify
import json
import random
import os
from datetime import datetime
import openai
from config import *

app = Flask(__name__)

# OpenAI Configuration
openai.api_key = OPENAI_API_KEY

def get_openai_response(user_message, conversation_history=None):
    """Get response from OpenAI API"""
    try:
        # Prepare messages for the API
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        # Add conversation history if available
        if conversation_history:
            for msg in conversation_history[-10:]:  # Keep last 10 messages for context
                messages.append(msg)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            presence_penalty=PRESENCE_PENALTY,
            frequency_penalty=FREQUENCY_PENALTY
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        
        # Check for specific quota error
        if "quota" in str(e).lower() or "exceeded" in str(e).lower():
            quota_responses = [
                "I'm currently experiencing API quota limitations. Please check your OpenAI billing or try the hardcoded version (app.py) for now.",
                "OpenAI API quota exceeded. You can continue chatting with the hardcoded version by running 'python app.py' instead.",
                "API quota limit reached. For immediate use, try the hardcoded chatbot version.",
                "OpenAI service is currently limited due to quota. Switch to the hardcoded version for instant responses."
            ]
            return random.choice(quota_responses)
        
        # General fallback responses for other errors
        fallback_responses = [
            "I'm having trouble connecting to OpenAI right now. Please try again in a moment.",
            "Sorry, I'm experiencing some technical difficulties. Let's continue our conversation!",
            "I'm not able to respond properly at the moment. Please try again later.",
            "There seems to be a connection issue. How about we chat about something else?"
        ]
        return random.choice(fallback_responses)

def get_bot_response(user_input):
    """Get bot response using OpenAI API"""
    return get_openai_response(user_input)

@app.route('/')
def index():
    return render_template('index.html', title="Chat + OpenAI", subtitle="AI-Powered Responses")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message.strip():
        return jsonify({'response': 'Please say something!'})
    
    bot_response = get_bot_response(user_message)
    
    return jsonify({
        'response': bot_response,
        'timestamp': datetime.now().strftime('%H:%M')
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint to verify OpenAI connection"""
    try:
        # Test OpenAI connection with a simple request
        test_response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        return jsonify({
            'status': 'healthy',
            'openai_connected': True,
            'message': 'OpenAI API is working correctly'
        })
    except Exception as e:
        error_msg = str(e)
        if "quota" in error_msg.lower() or "exceeded" in error_msg.lower():
            return jsonify({
                'status': 'quota_exceeded',
                'openai_connected': False,
                'error': error_msg,
                'message': 'OpenAI API quota exceeded. Please check your billing or use the hardcoded version.'
            })
        else:
            return jsonify({
                'status': 'unhealthy',
                'openai_connected': False,
                'error': error_msg,
                'message': 'OpenAI API connection failed. Please check your API key.'
            })

if __name__ == '__main__':
    # Check if OpenAI API key is configured
    if OPENAI_API_KEY == 'your-openai-api-key-here':
        print("⚠️  WARNING: OpenAI API key not configured!")
        print("Please set your OpenAI API key in the config.py file")
        print("You can get an API key from: https://platform.openai.com/api-keys")
        print("The chatbot will use fallback responses until configured.")
    
    print("🤖 Starting AI Chatbot with OpenAI Integration")
    print("🌐 Server will be available at: http://localhost:5000")
    print("🔗 Health check: http://localhost:5000/api/health")
    print("💡 If you see quota errors, try the hardcoded version: python app.py")
    
    app.run(debug=FLASK_DEBUG, host=FLASK_HOST, port=FLASK_PORT)
