from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS
import speech_recognition as sr
import requests
import io
from langdetect import detect
import re
from pydub import AudioSegment


app = Flask(__name__)
CORS(app)

conversation_history = ""



def format_chat_history(history_text):
    """
    Convert conversation history into HTML with colors:
    - "You:" in bold red
    - "LMStudio:" in bold green
    """
    formatted_lines = []
    for line in history_text.split("\n"):
        if line.startswith("You:"):
            formatted_lines.append(
                line.replace(
                    "You:", '<span style="color:red; font-weight:bold;">You:</span>'
                )
            )
        elif line.startswith("LMStudio:"):
            formatted_lines.append(
                line.replace(
                    "LMStudio:", '<span style="color:green; font-weight:bold;">LMStudio:</span>'
                )
            )
        else:
            formatted_lines.append(line)
    return "<br>".join(formatted_lines)



def clean_lm_response(raw_text):
    match = re.search(r"<\|channel\|>final<\|message\|>(.*)", raw_text, re.DOTALL)
    if match:
        text = match.group(1)
    else:
        text = raw_text
    text = re.sub(r"<\|.*?\|>", "", text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()

def ask_local_model(prompt):
    global conversation_history
    conversation_history += f"User: {prompt}\nAssistant:"

    payload = {
        "prompt": conversation_history,
        "max_tokens": 200,
        "temperature": 0.7,
        "stop": ["User:", "Assistant:"]
    }

    try:
        response = requests.post("http://localhost:1234/v1/completions", json=payload)
        response.raise_for_status()
        output = response.json()
        raw_text = output.get("choices", [{}])[0].get("text", "")
        cleaned_text = clean_lm_response(raw_text)
        conversation_history += f" {cleaned_text}\n"
        return cleaned_text
    except Exception as e:
        return f"Error contacting LMStudio: {e}"

@app.route("/text_query", methods=["POST"])
def text_query():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400
        answer = ask_local_model(prompt)
        
        formatted_history = format_chat_history(conversation_history)
        return jsonify({"answer": answer, "history": formatted_history})

    except Exception as e:
        return jsonify({"error": f"Internal error: {e}"}), 500

@app.route("/audio_query", methods=["POST"])
def audio_query():
    try:
        if "audio" not in request.files:
            return jsonify({"error": "No audio file provided"}), 400

        audio_file = request.files["audio"]
        audio_bytes = audio_file.read()

        # Convert WebM/Opus (from browser mic) to WAV
        audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
        wav_io = io.BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)

        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_io) as source:
            audio_data = recognizer.record(source)

        # try:
        #     user_text = recognizer.recognize_google(audio_data, language="fa-IR")
        #     detected_lang = "fa"
        # except sr.UnknownValueError:
        #     user_text = recognizer.recognize_google(audio_data, language="en-US")
        #     detected_lang = "en"

        user_text = recognizer.recognize_google(audio_data, language="en-US")
        detected_lang = "en"

        answer = ask_local_model(user_text)

        formatted_history = format_chat_history(conversation_history)

        return jsonify({
            "user_text": user_text,
            "language": detected_lang,
            "answer": answer,
            "history": formatted_history
        })

    except Exception as e:
        return jsonify({"error": f"Failed to process audio: {e}"}), 500

@app.route("/")
def serve_index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
