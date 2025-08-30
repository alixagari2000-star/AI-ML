#!/usr/bin/env python3
"""
Check OpenAI API Status
This script checks if your OpenAI API key is working and provides helpful information.
"""

import openai
from config import OPENAI_API_KEY

def check_api_status():
    print("🔍 Checking OpenAI API Status...")
    print("=" * 50)
    
    # Check if API key is configured
    if OPENAI_API_KEY == 'your-openai-api-key-here':
        print("❌ API key not configured!")
        print("Please set your OpenAI API key in config.py")
        return False
    
    print(f"✅ API key configured: {OPENAI_API_KEY[:20]}...")
    
    # Set the API key
    openai.api_key = OPENAI_API_KEY
    
    try:
        # Test with a simple request
        print("🧪 Testing API connection...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        
        print("✅ API connection successful!")
        print(f"Response: {response.choices[0].message.content}")
        print("\n🎉 Your OpenAI API is working correctly!")
        return True
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ API Error: {error_msg}")
        
        if "quota" in error_msg.lower() or "exceeded" in error_msg.lower():
            print("\n💰 QUOTA EXCEEDED")
            print("Your OpenAI API quota has been exceeded.")
            print("\nSolutions:")
            print("1. Check your OpenAI billing at: https://platform.openai.com/account/billing")
            print("2. Add payment method or increase quota")
            print("3. Use the hardcoded version: python app.py")
            print("4. Wait for quota reset (usually monthly)")
            
        elif "invalid" in error_msg.lower() or "authentication" in error_msg.lower():
            print("\n🔑 INVALID API KEY")
            print("Your API key appears to be invalid.")
            print("\nSolutions:")
            print("1. Get a new API key from: https://platform.openai.com/api-keys")
            print("2. Update the key in config.py")
            
        elif "rate" in error_msg.lower():
            print("\n⚡ RATE LIMIT")
            print("You've hit the rate limit.")
            print("\nSolutions:")
            print("1. Wait a few minutes and try again")
            print("2. Use the hardcoded version: python app.py")
            
        else:
            print("\n🔧 UNKNOWN ERROR")
            print("An unexpected error occurred.")
            print("\nSolutions:")
            print("1. Check your internet connection")
            print("2. Try again later")
            print("3. Use the hardcoded version: python app.py")
        
        return False

def main():
    print("🤖 OpenAI API Status Checker")
    print("=" * 50)
    
    success = check_api_status()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ You can now use the OpenAI chatbot: python appOAI.py")
    else:
        print("💡 For immediate use, try the hardcoded version: python app.py")
    
    print("\n📋 Available options:")
    print("- Hardcoded version (no API needed): python app.py")
    print("- OpenAI version (requires working API): python appOAI.py")
    print("- Check API status: python check_api_status.py")

if __name__ == "__main__":
    main()
