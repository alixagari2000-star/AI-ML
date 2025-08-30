#!/usr/bin/env python3
"""
Setup script for OpenAI API configuration
This script helps you set up your OpenAI API key for the chatbot
"""

import os
import sys

def setup_openai():
    print("🤖 OpenAI API Setup for AI Chatbot")
    print("=" * 50)
    print()
    
    print("To use OpenAI's GPT models, you need an API key.")
    print("1. Go to: https://platform.openai.com/api-keys")
    print("2. Sign up or log in to your OpenAI account")
    print("3. Create a new API key")
    print("4. Copy the API key (it starts with 'sk-')")
    print()
    
    # Check if API key is already set
    current_key = os.getenv('OPENAI_API_KEY', '')
    if current_key and current_key != 'your-openai-api-key-here':
        print(f"✅ API key already configured: {current_key[:10]}...")
        choice = input("Do you want to update it? (y/n): ").lower()
        if choice != 'y':
            print("Setup complete!")
            return
    
    # Get API key from user
    api_key = input("Enter your OpenAI API key (or press Enter to skip): ").strip()
    
    if not api_key:
        print("⚠️  No API key provided. The chatbot will use fallback responses.")
        print("You can set it later by editing config.py")
        return
    
    # Validate API key format
    if not api_key.startswith('sk-'):
        print("⚠️  Warning: API key doesn't start with 'sk-'. Please check your key.")
        choice = input("Continue anyway? (y/n): ").lower()
        if choice != 'y':
            return
    
    # Update config.py file
    try:
        config_path = 'config.py'
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the placeholder API key
        updated_content = content.replace(
            "OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-openai-api-key-here')",
            f"OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '{api_key}')"
        )
        
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print("✅ API key successfully configured!")
        print("You can now run the chatbot with: python app.py")
        
    except Exception as e:
        print(f"❌ Error updating config: {e}")
        print("Please manually edit config.py and set your API key")

def test_connection():
    """Test the OpenAI connection"""
    print("\n🧪 Testing OpenAI Connection...")
    
    try:
        import openai
        from config import OPENAI_API_KEY
        
        if OPENAI_API_KEY == 'your-openai-api-key-here':
            print("❌ API key not configured")
            return False
        
        openai.api_key = OPENAI_API_KEY
        
        # Test with a simple request
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        
        print("✅ OpenAI connection successful!")
        print(f"Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    setup_openai()
    
    # Ask if user wants to test connection
    choice = input("\nTest OpenAI connection? (y/n): ").lower()
    if choice == 'y':
        test_connection()
    
    print("\n🎉 Setup complete! Run 'python app.py' to start the chatbot.")
