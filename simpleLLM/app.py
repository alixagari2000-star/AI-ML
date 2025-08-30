from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_prompt = request.json.get('prompt', '')
    # Mock LLM response
    response = f"Echo: {user_prompt}"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)