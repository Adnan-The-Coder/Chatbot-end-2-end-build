print("Loading chatbot...")
import json
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


print("Importing Preferences")
nltk.download("punkt")

# Load intents
with open("data/datanyx-general-info.json", "r") as file:
    intents = json.load(file)

# Prepare training data
tags = []
patterns = []
for intent in intents:
    for pattern in intent["patterns"]:
        tags.append(intent["tag"])
        patterns.append(pattern)

# Initialize and train model
vectorizer = TfidfVectorizer()
classifier = LogisticRegression(random_state=0, max_iter=10000)

x = vectorizer.fit_transform(patterns)
y = tags
classifier.fit(x, y)

# Chatbot response function
def chatbot_response(text: str) -> str:
    input_text = vectorizer.transform([text])
    tag = classifier.predict(input_text)[0]
    for intent in intents:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "Sorry, I didn't understand that."
