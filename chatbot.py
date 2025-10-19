import json
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class Chatbot:
    def __init__(self, file_path: str):
        print("Loading chatbot...")
        self.file_path = file_path
        
        print("Importing Preferences")
        nltk.download("punkt")
        
        # Load intents from the given file path
        self.intents = self.load_intents()
        
        # Initialize the model components
        self.vectorizer = TfidfVectorizer()
        self.classifier = LogisticRegression(random_state=0, max_iter=10000)
        
        # Train the model
        self.train_model()
    
    def load_intents(self):
        """Load the intents from a JSON file"""
        with open(self.file_path, "r") as file:
            return json.load(file)

    def train_model(self):
        """Prepare the training data and train the classifier"""
        tags = []
        patterns = []
        
        for intent in self.intents:
            for pattern in intent["patterns"]:
                tags.append(intent["tag"])
                patterns.append(pattern)
        
        x = self.vectorizer.fit_transform(patterns)
        y = tags
        self.classifier.fit(x, y)
    
    def get_response(self, text: str) -> str:
        """Generate a chatbot response based on the input text"""
        input_text = self.vectorizer.transform([text])
        tag = self.classifier.predict(input_text)[0]
        
        for intent in self.intents:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])
        
        return "Sorry, I didn't understand that."

