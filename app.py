try:
    import nltk
    nltk.download('brown')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
except:
    pass

import streamlit as st
import joblib
from textblob import TextBlob
import re

# Load saved model and vectorizer
model = joblib.load("logistic_model.joblib")
vectorizer = joblib.load("tfidf_vectorizer.joblib")

# Label mapping based on your training data categories
label_mapping = {
    'Academic': 'Academic',
    'Admin/HR': 'Admin/HR',
    'Finance': 'Finance',
    'Hostel': 'Hostel',
    'IT Support': 'IT Support',
    'Library': 'Library'
}

# Protected words you don’t want to auto-correct
PROTECTED_WORDS = {"hostel", "admin", "wifi", "it", "library", "academic", "finance"}

def smart_correct(text):
    words = text.split()
    corrected_words = []
    for word in words:
        if word.lower() in PROTECTED_WORDS:
            corrected_words.append(word)
        else:
            corrected = str(TextBlob(word).correct())
            corrected_words.append(corrected)
    corrected_text = " ".join(corrected_words)
    corrected_text = corrected_text.lower()
    corrected_text = re.sub(r'[^\w\s]', '', corrected_text)
    corrected_text = re.sub(r'\s+', ' ', corrected_text).strip()
    return corrected_text

def predict_category(text):
    cleaned = smart_correct(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    return pred

st.title("🎓 College Complaint Classifier")
st.write("Enter your complaint below. The app will predict the relevant department.")

complaint = st.text_area("📝 Complaint Text")

if st.button("🔍 Predict Department"):
    if complaint.strip() == "":
        st.warning("Please enter a complaint.")
    else:
        category = predict_category(complaint)
        st.success(f"✅ Predicted Department: **{category}**")
