# chat_with_model.py
import joblib

# Load model + vectorizer
model, vectorizer = joblib.load("tiny_model.pkl")

def get_response(user_input):
    X = vectorizer.transform([user_input])
    prediction = model.predict(X)[0]

    # Check if it's close to known phrases
    if user_input in ["Hi", "my name is Ali", "Bye"]:
        return prediction
    else:
        return "shut up"

# Interactive loop
if __name__ == "__main__":
    print("Type something (or 'exit' to quit):")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break
        print(get_response(user_input))
