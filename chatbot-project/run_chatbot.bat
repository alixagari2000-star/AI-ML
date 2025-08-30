@echo off
echo Starting AI Chatbot...
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting the chatbot server...
echo.
echo The chatbot will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
