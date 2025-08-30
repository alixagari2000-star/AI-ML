# Flutter Reminder App

A cross-platform mobile app built with Flutter that allows users to set future reminders with custom descriptions and receive notifications at the specified date and time. Works on both Android and iOS devices.

## 🚀 Features

- **Cross-Platform**: Works on Android and iOS
- **Date & Time Selection**: Pick any future date and time
- **Custom Description**: Enter reminder text (up to 40 characters)
- **One-time Notifications**: Receive a single notification at the specified time
- **Modern UI**: Clean Material Design interface
- **Permission Handling**: Automatic notification permission requests
- **Validation**: Ensures future dates and non-empty descriptions
- **Success Feedback**: Visual confirmation when reminder is set

## 📋 Requirements

- **Flutter SDK**: 3.0.0 or later
- **Dart SDK**: 3.0.0 or later
- **Android**: API level 21 or later
- **iOS**: iOS 11.0 or later
- **Device**: Android phone or iPhone

## 🛠️ Installation & Setup

### 1. Install Flutter

If you haven't installed Flutter yet:

1. **Download Flutter SDK** from [flutter.dev](https://flutter.dev/docs/get-started/install)
2. **Add Flutter to PATH** environment variable
3. **Run `flutter doctor`** to verify installation

### 2. Clone/Download the Project

1. **Navigate to the project directory**:
   ```bash
   cd C:\Users\AA2\flutter-reminder-app
   ```

2. **Install dependencies**:
   ```bash
   flutter pub get
   ```

### 3. Run the App

#### For Android:
1. **Connect your Android device** via USB
2. **Enable USB debugging** on your device
3. **Run the app**:
   ```bash
   flutter run
   ```

#### For iOS (requires Mac):
1. **Connect your iPhone** via USB
2. **Open iOS Simulator** or use physical device
3. **Run the app**:
   ```bash
   flutter run
   ```

#### For Web (testing):
```bash
flutter run -d chrome
```

## 📱 Usage

### Setting a Reminder
1. **Select Date & Time**: Tap the date/time field to open pickers
2. **Enter Description**: Type your reminder text (max 40 characters)
3. **Tap "Remind Me"**: The button enables when valid input is provided
4. **Confirm**: You'll see a success message confirming the reminder is set

### Notification
- You'll receive a notification at the exact time you specified
- The notification will display your custom description
- Includes sound and vibration (if enabled)

## 🏗️ Project Structure

```
flutter-reminder-app/
├── lib/
│   └── main.dart              # Main app file with UI and logic
├── android/                   # Android-specific configuration
│   └── app/src/main/
│       └── AndroidManifest.xml
├── ios/                      # iOS-specific configuration
│   └── Runner/
│       └── Info.plist
├── pubspec.yaml              # Dependencies and project config
└── README.md                 # This file
```

## 🔧 Dependencies

- **flutter_local_notifications**: Local notification scheduling
- **timezone**: Timezone handling for notifications
- **intl**: Date/time formatting
- **permission_handler**: Permission management

## 🎨 UI Components

- **Material Design**: Modern, clean interface
- **Cards**: Organized content sections
- **Date/Time Pickers**: Native platform pickers
- **Form Validation**: Real-time input validation
- **Success Feedback**: Visual confirmation animations

## 📱 Platform Support

### Android
- ✅ Notification permissions
- ✅ Background notification scheduling
- ✅ Material Design components
- ✅ API level 21+ support

### iOS
- ✅ Notification permissions
- ✅ Local notification scheduling
- ✅ iOS-style components
- ✅ iOS 11.0+ support

## 🚨 Troubleshooting

### Common Issues

1. **Flutter not found**:
   - Ensure Flutter is installed and in PATH
   - Run `flutter doctor` to check installation

2. **Dependencies not found**:
   ```bash
   flutter pub get
   ```

3. **Android device not detected**:
   - Enable USB debugging
   - Install Android drivers
   - Check device connection

4. **Notifications not working**:
   - Grant notification permissions
   - Check device notification settings
   - Test on physical device (not emulator)

5. **Build errors**:
   ```bash
   flutter clean
   flutter pub get
   flutter run
   ```

### Debug Commands

```bash
# Check Flutter installation
flutter doctor

# Get dependencies
flutter pub get

# Clean build
flutter clean

# Run with verbose output
flutter run -v

# Check connected devices
flutter devices
```

## 🔄 Development

### Adding Features
1. **Modify `lib/main.dart`** for UI changes
2. **Update `pubspec.yaml`** for new dependencies
3. **Test on both platforms** for compatibility

### Customization
- **Colors**: Modify `ThemeData` in main.dart
- **Text**: Update strings in the UI
- **Validation**: Modify `_isValidInput()` method
- **Notifications**: Adjust notification settings

## 📄 License

This project is provided as-is for educational and development purposes.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test on both platforms
5. Submit a pull request

---

## 🎯 Quick Start

1. **Install Flutter** (if not already installed)
2. **Navigate to project**: `cd C:\Users\AA2\flutter-reminder-app`
3. **Install dependencies**: `flutter pub get`
4. **Connect device** (Android phone or iPhone)
5. **Run app**: `flutter run`
6. **Grant permissions** when prompted
7. **Set a test reminder** for 1-2 minutes in the future
8. **Wait for notification** to appear

**Enjoy your cross-platform reminder app!** 📱⏰✨
