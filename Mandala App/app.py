# app.py

import streamlit as st
from openai import OpenAI

# --- Page Setup ---
st.set_page_config(page_title="Mandala Generator", layout="centered")
st.title("🌀 Mandala Art Generator")
st.write("Enter a word and get a beautiful mandala inspired by it.")

# --- API Key Input ---
api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

# --- Word Input ---
word = st.text_input("🎨 Enter a word for the mandala design")

# --- Generate Button ---
if st.button("🖼️ Generate Mandala"):

    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not word.strip():
        st.error("Please enter a word.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            prompt = f"A detailed mandala art inspired by the word '{word}'"

            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1
            )

            image_url = response.data[0].url
            st.image(image_url, caption=f"Mandala inspired by '{word}'", use_column_width=True)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
