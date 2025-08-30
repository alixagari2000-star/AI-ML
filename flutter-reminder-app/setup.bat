@echo off
echo ========================================
echo    Flutter Reminder App Setup
echo ========================================
echo.

echo Checking Flutter installation...
flutter --version
if %errorlevel% neq 0 (
    echo ERROR: Flutter is not installed or not in PATH
    echo Please install Flutter from: https://flutter.dev/docs/get-started/install
    pause
    exit /b 1
)

echo.
echo Installing dependencies...
flutter pub get
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Checking connected devices...
flutter devices

echo.
echo ========================================
echo Setup complete! 
echo.
echo To run the app:
echo 1. Connect your Android phone or iPhone
echo 2. Run: flutter run
echo 3. Grant notification permissions when prompted
echo.
echo For web testing: flutter run -d chrome
echo ========================================
pause
