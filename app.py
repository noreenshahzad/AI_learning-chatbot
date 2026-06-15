import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🤖 AI Learning Chatbot")

# Load data
with open("training_data.txt", "r", encoding="utf-8") as f:
    data = f.readlines()

data = [d.strip() for d in data if d.strip()]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(data)

user_input = st.text_input("💬 Ask your question:")

if user_input:
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, vectors)

    index = similarity.argmax()

    st.write("🤖 Bot Answer:")
    st.success(data[index])