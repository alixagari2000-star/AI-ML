import SwiftUI
import UserNotifications

@main
struct ReminderApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

struct ContentView: View {
    @State private var selectedDate = Date()
    @State private var reminderDescription = ""
    @State private var showingAlert = false
    @State private var alertMessage = ""
    @State private var isReminderSet = false
    
    var body: some View {
        NavigationView {
            VStack(spacing: 30) {
                // Header
                VStack {
                    Text("Reminder App")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .foregroundColor(.primary)
                    
                    Text("Set your future reminder")
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                }
                .padding(.top, 20)
                
                // Date and Time Picker
                VStack(alignment: .leading, spacing: 10) {
                    Text("Select Date & Time")
                        .font(.headline)
                        .foregroundColor(.primary)
                    
                    DatePicker("", selection: $selectedDate, in: Date()..., displayedComponents: [.date, .hourAndMinute])
                        .datePickerStyle(WheelDatePickerStyle())
                        .labelsHidden()
                        .background(Color(.systemGray6))
                        .cornerRadius(10)
                }
                .padding(.horizontal, 20)
                
                // Description Input
                VStack(alignment: .leading, spacing: 10) {
                    Text("Reminder Description")
                        .font(.headline)
                        .foregroundColor(.primary)
                    
                    TextField("Enter your reminder (max 40 characters)", text: $reminderDescription)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                        .onChange(of: reminderDescription) { newValue in
                            if newValue.count > 40 {
                                reminderDescription = String(newValue.prefix(40))
                            }
                        }
                    
                    Text("\(reminderDescription.count)/40 characters")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
                .padding(.horizontal, 20)
                
                // Remind Me Button
                Button(action: setReminder) {
                    HStack {
                        Image(systemName: "bell.fill")
                            .foregroundColor(.white)
                        Text("Remind Me")
                            .fontWeight(.semibold)
                            .foregroundColor(.white)
                    }
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(selectedDate > Date() && !reminderDescription.isEmpty ? Color.blue : Color.gray)
                    .cornerRadius(10)
                }
                .disabled(selectedDate <= Date() || reminderDescription.isEmpty)
                .padding(.horizontal, 20)
                
                // Status Display
                if isReminderSet {
                    VStack {
                        Image(systemName: "checkmark.circle.fill")
                            .foregroundColor(.green)
                            .font(.title)
                        Text("Reminder Set Successfully!")
                            .font(.headline)
                            .foregroundColor(.green)
                        Text("You'll be notified at \(formatDate(selectedDate))")
                            .font(.caption)
                            .foregroundColor(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding()
                    .background(Color(.systemGray6))
                    .cornerRadius(10)
                    .padding(.horizontal, 20)
                }
                
                Spacer()
            }
            .navigationBarHidden(true)
        }
        .alert("Reminder", isPresented: $showingAlert) {
            Button("OK") { }
        } message: {
            Text(alertMessage)
        }
        .onAppear {
            requestNotificationPermission()
        }
    }
    
    private func requestNotificationPermission() {
        UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .badge, .sound]) { granted, error in
            if let error = error {
                print("Notification permission error: \(error)")
            }
        }
    }
    
    private func setReminder() {
        guard selectedDate > Date() else {
            alertMessage = "Please select a future date and time."
            showingAlert = true
            return
        }
        
        guard !reminderDescription.isEmpty else {
            alertMessage = "Please enter a reminder description."
            showingAlert = true
            return
        }
        
        let content = UNMutableNotificationContent()
        content.title = "Reminder"
        content.body = reminderDescription
        content.sound = .default
        
        let triggerDate = Calendar.current.dateComponents([.year, .month, .day, .hour, .minute], from: selectedDate)
        let trigger = UNCalendarNotificationTrigger(dateMatching: triggerDate, repeats: false)
        
        let request = UNNotificationRequest(identifier: UUID().uuidString, content: content, trigger: trigger)
        
        UNUserNotificationCenter.current().add(request) { error in
            DispatchQueue.main.async {
                if let error = error {
                    alertMessage = "Failed to set reminder: \(error.localizedDescription)"
                    showingAlert = true
                } else {
                    isReminderSet = true
                    // Reset form after successful reminder set
                    DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
                        isReminderSet = false
                        reminderDescription = ""
                        selectedDate = Date()
                    }
                }
            }
        }
    }
    
    private func formatDate(_ date: Date) -> String {
        let formatter = DateFormatter()
        formatter.dateStyle = .medium
        formatter.timeStyle = .short
        return formatter.string(from: date)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
