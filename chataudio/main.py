import speech_recognition as sr
import requests
import pyttsx3

# Text-to-speech engine 
engine = pyttsx3.init()

def ask_local_model(prompt):
    url = "http://localhost:1234/v1/completions"
    payload = {
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.7,
        "stop": None,
        "model": "local-model",  # Optional: if multiple models are loaded
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        output = response.json()
        print(f"🔍 Raw response from LM: {output}")
        return output.get("choices", [{}])[0].get("text", "").strip()
    except Exception as e:
        return f"Error contacting local LM: {e}"



recognizer = sr.Recognizer()
mic = sr.Microphone()

print("🎤 Say something! (Ctrl+C to stop)")
 
with mic as source:
    recognizer.adjust_for_ambient_noise(source)

    while True:
        try:
            audio = recognizer.listen(source)
            user_text = recognizer.recognize_google(audio)
            print(f"🗣 You said: {user_text}")

            reply = ask_local_model(user_text)
            print(f"🤖 Local LM: {reply}\n")

            #engine.say(reply)
            #engine.runAndWait()

        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
        except KeyboardInterrupt:
            print("\n👋 Stopping.")
            break
