from flask import Flask, render_template, request, jsonify
import json
import random
from datetime import datetime

app = Flask(__name__)

# Conversation data
conversation_data = {
    "greetings": {
        "user_inputs": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
        "bot_responses": [
            "Hello! How can I help you today?",
            "Hi there! Nice to meet you!",
            "Hey! Welcome to our conversation!",
            "Hello! I'm here to chat with you!",
            "Hi dear! How are you doing?"
        ]
    },
    "farewells": {
        "user_inputs": ["bye", "goodbye", "see you", "take care", "exit", "quit"],
        "bot_responses": [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! It was nice chatting with you!",
            "Take care! Come back soon!",
            "Goodbye! Looking forward to our next conversation!"
        ]
    },
    "how_are_you": {
        "user_inputs": ["how are you", "how are you doing", "are you ok", "how do you feel"],
        "bot_responses": [
            "I'm doing great, thank you for asking! How about you?",
            "I'm wonderful! Thanks for caring. How are you?",
            "I'm fine and ready to chat! How are you doing?",
            "I'm doing well! How's your day going?",
            "I'm excellent! How about yourself?"
        ]
    },
    "thanks": {
        "user_inputs": ["thank you", "thanks", "thank you so much", "appreciate it"],
        "bot_responses": [
            "You're welcome! I'm happy to help!",
            "No problem at all!",
            "My pleasure!",
            "Anytime! That's what I'm here for!",
            "You're very welcome!"
        ]
    },
    "weather": {
        "user_inputs": ["weather", "temperature", "hot", "cold", "sunny", "rainy"],
        "bot_responses": [
            "I can't check the weather, but I hope it's nice where you are!",
            "Weather is always a great conversation topic! What's it like where you are?",
            "I'd love to know about the weather where you are!",
            "Weather can really affect our mood, don't you think?",
            "I hope the weather is pleasant for you today!"
        ]
    }
}

def get_bot_response(user_input):
    """Get appropriate bot response based on user input"""
    user_input_lower = user_input.lower().strip()
    
    # Check each conversation category
    for category, data in conversation_data.items():
        if any(keyword in user_input_lower for keyword in data["user_inputs"]):
            return random.choice(data["bot_responses"])
    
    # Default responses for unrecognized input
    default_responses = [
        "That's interesting! Tell me more about that.",
        "I'm not sure I understand. Could you rephrase that?",
        "That's a good point! What do you think about it?",
        "I'd love to hear more about your thoughts on this.",
        "That's something to think about! What's your perspective?",
        "Interesting! How do you feel about that?",
        "I'm learning from our conversation! What else would you like to discuss?",
        "That's a great topic! What are your thoughts?",
        "I appreciate you sharing that with me. Tell me more!",
        "That's fascinating! What made you think of that?"
    ]
    
    return random.choice(default_responses)

@app.route('/')
def index():
    return render_template('index.html', title="Chat without OpenAI From Ali", subtitle="Hardcoded Responses for testing")

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

@app.route('/api/conversation-data')
def get_conversation_data():
    """API endpoint to get conversation data"""
    return jsonify(conversation_data)

if __name__ == '__main__':
    print("🤖 Starting Chatbot with Hardcoded Responses")
    print("🌐 Server will be available at: http://localhost:5000")
    print("📝 Using predefined conversation patterns")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
