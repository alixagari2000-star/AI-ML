@echo off
echo Starting OpenAI Chatbot...
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting the OpenAI chatbot server...
echo.
echo The chatbot will be available at: http://localhost:5000
echo This version uses OpenAI GPT for intelligent responses
echo Make sure you have configured your OpenAI API key
echo Press Ctrl+C to stop the server
echo.
python appOAI.py
pause
