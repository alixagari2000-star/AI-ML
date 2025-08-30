@echo off
echo Starting Hardcoded Chatbot...
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting the hardcoded chatbot server...
echo.
echo The chatbot will be available at: http://localhost:5000
echo This version uses predefined conversation patterns
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
