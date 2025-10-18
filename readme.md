
# 🤖 Simple Chatbot using Logistic Regression

This is a terminal-based chatbot implemented in Python using `scikit-learn`'s `LogisticRegression` classifier. The chatbot is trained on a set of intents defined in a JSON file and responds based on user input using machine learning and natural language processing.

---

## 📁 Project Structure

```

CHATBOT/
├── data/
│   └── datanyx-general-info.json   # Training data (intents and responses)
├── main.py                         # Chatbot script
├── Dockerfile                      # Docker configuration
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation

```

---

##  Features

- Simple text-based interaction in the terminal
- Trained using Logistic Regression from `scikit-learn`
- Uses TF-IDF vectorization for input processing
- Random response selection from matched intent
- Easily dockerizable and portable and deployable
- Github Actions CD Pipeline with Render Deployment

---

## 📦 Requirements

`requirements.txt` file has these following contents:

```
pip install -r requirements.txt
```

> 💡 **Note**: Even though `numpy` is not explicitly imported in `chatbot.py`, it is required by `scikit-learn` internally. Without it, the application will fail at runtime.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Adnan-The-Coder/Chatbot-end-end-build.git
```

### 2. Create and activate a virtual environment
```
python -m venv venv
```
Activate it in (Windows)
```
venv\Scripts\activate
```
OR (macOS/Linux)
```
source venv/bin/activate
```

### 3. Install Dependencies (Without Docker)

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI app
uvicorn api:app --reload


Visit: http://localhost:8000

Endpoint: POST /chat
```
{
  "message": "hi"
}
```

---

## 🐳 Running with Docker

### 1. Build the Docker Image

```bash
docker build -t ml-lr-chatbot .
```

### 2. Run the Docker Container

```bash
docker run -p 8080:8000 ml-lr-chatbot-api
```

---

## 🛠 API Overview
- Method:	POST
- Endpoint:	/chat
- Description: Get chatbot reply

##  How It Works

### Data Structure (`data/datanyx-general-info.json`)

The JSON file contains a list of **intents**:
You can add your own data of intents and update in main.py and build image and run accordingly

```json
[
  {
    "tag": "greeting",
    "patterns": ["Hi", "Hello", "How are you?"],
    "responses": ["Hello!", "Hi there!", "Greetings!"]
  },
  ...
]
```

### Training the Model

* The chatbot reads all `patterns` and `tags` from the JSON file.
* TF-IDF is used to vectorize the input patterns.
* Logistic Regression trains a classifier to map input text to the correct intent tag.

### Chatbot Workflow

1. Wait for user input.
2. Transform input using the trained TF-IDF vectorizer.
3. Predict the tag using the logistic regression model.
4. Find a matching intent and respond with a random reply from the associated `responses`.

---

## 📜 Code Overview

### Main Components of `main.py`

* **NLTK Setup**
  Downloads the `punkt` tokenizer needed for any NLTK processing.

* **Data Loading**

  ```python
  with open("data/datanyx-general-info.json", "r") as file:
      intents = json.load(file)
  ```

* **Model Training**

  ```python
  vectorizer = TfidfVectorizer()
  classifier = LogisticRegression(random_state=0, max_iter=10000)
  ```

* **Response Function**

  ```python
  def chatbot_response(text):
      input_text = vectorizer.transform([text])
      tag = classifier.predict(input_text)[0]
      ...
  ```

* **Main Loop**

  ```python
  while True:
      query = input("User-> ")
      output = chatbot_response(query)
      print(f"Chatbot-> {output}")
  ```

---

##  Notes

* `numpy` is a transitive dependency of `scikit-learn`. Without it, `TfidfVectorizer` or `LogisticRegression` will fail.
* This chatbot is **state-less** — it does not remember previous interactions.
* Suitable for educational purposes, simple internal bots, or extending into more advanced models like transformers.

---

##  To Do / Future Improvements

* Add GUI or web interface (e.g., with Flask)
* Save and load the trained model using `pickle`
* Use lemmatization or stemming for better NLP processing
* Support multiple intents per input

---

##  Author

**Adnan** – [@Adnan-The-Coder](https://github.com/Adnan-The-Coder)

