#!/usr/bin/env python3
"""
Test script for the AI Chatbot
This script tests the chatbot's response functionality without running the web server.
"""

import json
import random
from datetime import datetime

# Import the chatbot logic from app.py
def get_bot_response(user_input):
    """Get appropriate bot response based on user input"""
    
    # Conversation data (same as in app.py)
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

def test_chatbot():
    """Test the chatbot with various inputs"""
    
    print("🤖 AI Chatbot Test Suite")
    print("=" * 50)
    print()
    
    # Test cases
    test_cases = [
        "hello",
        "hi dear",
        "how are you",
        "thank you",
        "what's the weather like?",
        "goodbye",
        "tell me a joke",
        "what's your name?",
        "bye",
        "thanks a lot"
    ]
    
    print("Testing conversation patterns:")
    print("-" * 30)
    
    for i, test_input in enumerate(test_cases, 1):
        response = get_bot_response(test_input)
        print(f"Test {i:2d}: '{test_input}'")
        print(f"       Bot: {response}")
        print()
    
    print("=" * 50)
    print("✅ All tests completed!")
    print()
    print("To run the web interface:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run the server: python app.py")
    print("3. Open browser: http://localhost:5000")
    print()
    print("Or simply double-click: run_chatbot.bat")

if __name__ == "__main__":
    test_chatbot()
