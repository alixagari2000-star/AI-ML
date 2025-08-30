# iPhone Reminder App

A simple and elegant iOS app built with SwiftUI that allows users to set future reminders with custom descriptions and receive notifications at the specified date and time.

## Features

- **Date & Time Selection**: Pick any future date and time using the native iOS date picker
- **Custom Description**: Enter reminder text (up to 40 characters)
- **One-time Notifications**: Receive a single notification at the specified time
- **Modern UI**: Clean SwiftUI interface with intuitive design
- **Permission Handling**: Automatic notification permission requests
- **Validation**: Ensures future dates and non-empty descriptions
- **Success Feedback**: Visual confirmation when reminder is set

## Requirements

- **iOS**: 17.0 or later
- **Xcode**: 15.0 or later
- **Swift**: 5.0 or later
- **Device**: iPhone or iPad

## Installation & Setup

### 1. Open in Xcode
1. Open Xcode
2. Select "Open a project or file"
3. Navigate to the `iphone-reminder-app` folder
4. Select the project file

### 2. Configure Project
1. Select the project in the navigator
2. Choose your development team
3. Update the Bundle Identifier if needed
4. Ensure notification capabilities are enabled

### 3. Build and Run
1. Select your target device (iPhone simulator or physical device)
2. Press `Cmd + R` to build and run
3. Grant notification permissions when prompted

## Usage

### Setting a Reminder
1. **Select Date & Time**: Use the wheel picker to choose a future date and time
2. **Enter Description**: Type your reminder text (max 40 characters)
3. **Tap "Remind Me"**: The button will be enabled when valid input is provided
4. **Confirm**: You'll see a success message confirming the reminder is set

### Notification
- You'll receive a notification at the exact time you specified
- The notification will display your custom description
- Includes sound and badge (if enabled)

## Technical Details

### Architecture
- **Framework**: SwiftUI
- **Notifications**: UserNotifications framework
- **State Management**: @State properties for reactive UI
- **Validation**: Real-time input validation and feedback

### Key Components
- `ReminderApp.swift`: Main app entry point
- `ContentView.swift`: Main UI and business logic
- `Info.plist`: App configuration and permissions
- `project.pbxproj`: Xcode project configuration

### Permissions
The app requests the following permissions:
- **Notifications**: Required for sending reminders
- **Alert**: Display notification banners
- **Badge**: Show app badge with notification count
- **Sound**: Play notification sounds

## File Structure

```
iphone-reminder-app/
├── ReminderApp.swift          # Main app file
├── project.pbxproj           # Xcode project configuration
├── Info.plist               # App configuration and permissions
└── README.md                # This file
```

## Customization

### Modify Reminder Behavior
- Change notification sound in `setReminder()` function
- Adjust character limit in the TextField validation
- Modify success message duration

### UI Customization
- Update colors and styling in `ContentView`
- Modify date picker style and components
- Customize button appearance and animations

### Notification Settings
- Add custom notification categories
- Implement notification actions
- Configure notification scheduling options

## Troubleshooting

### Common Issues
1. **Notifications not working**: Ensure permissions are granted in Settings
2. **Build errors**: Check Xcode version compatibility
3. **Simulator issues**: Test on physical device for notifications

### Debug Tips
- Check notification center for pending notifications
- Verify date/time selection is in the future
- Monitor console for permission errors

## Future Enhancements

- Multiple reminders management
- Recurring reminders
- Custom notification sounds
- Reminder categories/tags
- Cloud sync support
- Widget integration

## License

This project is provided as-is for educational and development purposes.

---

**Note**: This app requires notification permissions to function properly. Users will be prompted to allow notifications when the app is first launched.
