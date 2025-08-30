# train_and_save.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Training data
X_train = ["Hi", "my name is Ali", "Bye"]
y_train = ["hellop", "nice", "Hell"]

# Convert text to simple bag-of-words
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X_train)

# Train a small classifier
model = LogisticRegression()
model.fit(X_vec, y_train)

# Save both model + vectorizer
joblib.dump((model, vectorizer), "tiny_model.pkl")
print("Model saved as tiny_model.pkl")
