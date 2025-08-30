# Reminder App Demo Guide

## Quick Demo Setup

### 1. Test with Simulator
1. Open the project in Xcode
2. Select iPhone Simulator as target
3. Set a reminder for 1-2 minutes in the future
4. Wait for the notification to appear

### 2. Test with Physical Device
1. Connect your iPhone to Mac
2. Select your device as target
3. Trust the developer certificate if prompted
4. Set a reminder and test notifications

## Demo Scenarios

### Scenario 1: Basic Reminder
1. Open the app
2. Select a time 2 minutes from now
3. Enter: "Test reminder"
4. Tap "Remind Me"
5. Wait for notification

### Scenario 2: Character Limit Test
1. Try entering more than 40 characters
2. Notice it automatically truncates
3. See the character counter update

### Scenario 3: Validation Test
1. Try to set a past date
2. Notice the button stays disabled
3. Try with empty description
4. See validation in action

### Scenario 4: Success Feedback
1. Set a valid reminder
2. Watch the success animation
3. See the form reset after 3 seconds

## Expected Behaviors

### UI Elements
- ✅ Date picker shows future dates only
- ✅ Character counter updates in real-time
- ✅ Button enables/disables based on validation
- ✅ Success message appears after setting reminder
- ✅ Form resets automatically

### Notifications
- ✅ Permission request on first launch
- ✅ Notification appears at exact time
- ✅ Shows custom description
- ✅ Includes sound and badge
- ✅ One-time notification (no repeats)

### Error Handling
- ✅ Past dates are rejected
- ✅ Empty descriptions are rejected
- ✅ Clear error messages
- ✅ Graceful permission handling

## Troubleshooting Demo Issues

### Notification Not Working?
1. Check Settings > Notifications > Reminder App
2. Ensure permissions are granted
3. Test on physical device (simulator has limitations)

### Build Errors?
1. Check Xcode version (15.0+ required)
2. Verify iOS deployment target (17.0+)
3. Clean build folder (Cmd + Shift + K)

### UI Issues?
1. Check device orientation support
2. Verify SwiftUI preview compatibility
3. Test on different screen sizes

## Performance Notes

- App launches quickly
- UI responds immediately to input
- Notifications are scheduled efficiently
- Memory usage is minimal
- Battery impact is negligible

---

**Tip**: For the best demo experience, test on a physical iPhone device where notifications work properly.
