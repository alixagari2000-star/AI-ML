import speech_recognition as sr
import requests
import keyboard  # pip install keyboard
import threading
import time
import re
from langdetect import detect  # NEW
import json

def clean_lm_response(raw_text):
    # Step 1: Extract only the final assistant message
    match = re.search(r"<\|channel\|>final<\|message\|>(.*)", raw_text, re.DOTALL)
    if match:
        text = match.group(1)
    else:
        # Fallback: Use everything, even if format is unexpected
        text = raw_text

    # Step 2: Remove any leftover tags like <|...|>
    text = re.sub(r"<\|.*?\|>", "", text)

    # Step 3: Clean up whitespace
    text = text.strip()
    text = re.sub(r'\n+', '\n', text)

    return text






conversation_history = ""

def ask_local_model(prompt):
    global conversation_history
    conversation_history += f"User: {prompt}\nAssistant:"


    # 👇 Print the conversation history before sending request
    print("🧾 Conversation history being sent to LMStudio:")
    print("-------------------------------------------------")
    print(conversation_history)
    print("-------------------------------------------------\n")


    url = "http://localhost:1234/v1/completions"
    payload = {
        "prompt": conversation_history,
        "max_tokens": 200,
        "temperature": 0.7
        ,"stop": ["User:", "Assistant:"]    # to speed up, comment this line
    }


    # ✅ Debug: print the full payload
    print("📤 Payload being sent to LM Studio:")
    print(json.dumps(payload, indent=2, ensure_ascii=False))


    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        output = response.json()
        raw_text = output.get("choices", [{}])[0].get("text", "")

        cleaned_text = clean_lm_response(raw_text)

        # Add cleaned reply to history
        conversation_history += f" {cleaned_text}\n"

        return cleaned_text
    except Exception as e:
        return f"Error contacting local LM: {e}"



def listen_until_stop(recognizer, mic, stop_event):
    print("🎤 Listening... Press 'S' to stop.")
    audio_data = []

    def on_stop_key(e):
        if e.name.lower() == 's':
            stop_event.set()

    keyboard.on_press(on_stop_key)

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while not stop_event.is_set():
            try:
                audio = recognizer.listen(source, timeout=1, phrase_time_limit=5)
                audio_data.append(audio)
            except sr.WaitTimeoutError:
                pass

    keyboard.unhook_all()  # Remove the S key hook
    print("🛑 Stopped listening.")
    
    # Combine audio chunks if needed, or use the last one
    if not audio_data:
        return None
    # Use the last chunk for recognition
    return audio_data[-1]

def main():

    RLM = "\u200F"  # Right-to-left mark

    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Press 'L' to start listening, 'Q' to quit.")

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name.lower()
            if key == 'q':
                print("👋 Exiting.")
                break
            elif key == 'l':
                stop_event = threading.Event()
                audio = listen_until_stop(recognizer, mic, stop_event)
                if audio is None:
                    print("❌ No audio captured.")
                    continue

                try:
                    user_text = recognizer.recognize_google(audio)
                    print(f"🗣 You said: {user_text}")
                except sr.UnknownValueError:
                    print("❌ Could not understand audio.")
                    continue

                reply = ask_local_model(user_text)
                print(f"🤖 Local LM: {reply}\n")
                print("Press 'L' to start listening again, 'Q' to quit.")




if __name__ == "__main__":
    main()
