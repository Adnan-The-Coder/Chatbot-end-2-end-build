## Simple Chatbot using Logistic regression

print("Loading chatbot...")
print("Importing Preferences")
import json
import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


print("Downloading NLTK punkt package...")
nltk.download("punkt")

# Load intents from the JSON file
with open("data/datanyx-general-info.json", "r") as file:
    intents = json.load(file)

# Initialize the TF-IDF vectorizer and classifier
vectorizer = TfidfVectorizer()
classifier = LogisticRegression(random_state=0, max_iter=10000)

# Prepare the data for training
tags = []
patterns = []

for i in intents:
    for pattern in i['patterns']:
        tags.append(i["tag"])
        patterns.append(pattern)

# Transform the patterns using TF-IDF
x = vectorizer.fit_transform(patterns)
y = tags

# Train the classifier
classifier.fit(x, y)

# Function to get chatbot's response
def chatbot_response(text):
    input_text = vectorizer.transform([text])
    tagsdata = classifier.predict(input_text)[0]
    for i in intents:
        if i["tag"] == tagsdata:
            response = random.choice(i['responses'])
            return response

# Run the chatbot
while True:
    query = input("User-> ")
    output = chatbot_response(query)
    print(f"Chatbot-> {output}")
