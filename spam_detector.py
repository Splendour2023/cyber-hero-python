import pandas as pd
import csv  # ✅ Add this line

# ✅ Updated CSV reading to handle quotes and commas
data = pd.read_csv("spam_data.csv", quoting=csv.QUOTE_ALL, encoding="utf-8")

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# 📥 Load the dataset
data = pd.read_csv("spam_data.csv")

# 🏷️ Separate messages and labels (X = message, y = spam/ham)
X = data['text']
y = data['label']

# 🧼 Turn words into numbers so AI can understand
vectorizer = CountVectorizer()
X_vector = vectorizer.fit_transform(X)

# ✂️ Split data: some to train, some to test
X_train, X_test, y_train, y_test = train_test_split(X_vector, y, test_size=0.3, random_state=42)

# 🧠 Train the AI using Naive Bayes (a spam expert algorithm)
model = MultinomialNB()
model.fit(X_train, y_train)

# 🧪 Test it!
accuracy = model.score(X_test, y_test)
print(f"Spam Detector Accuracy: {accuracy * 100:.2f}%")

# 🧠 Predict a new message
test_message = ["Congratulations! You won free crypto."]
test_vector = vectorizer.transform(test_message)
prediction = model.predict(test_vector)
print(f"Prediction: {prediction[0]}")
