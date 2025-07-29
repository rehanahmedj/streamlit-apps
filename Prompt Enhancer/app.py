# app.py

import streamlit as st
from openai import OpenAI

# --- Page Config ---
st.set_page_config(page_title="Prompt Enhancer", layout="centered")
st.title("🔧 Prompt Enhancer App")
st.write("Improve your prompts using the power of OpenAI. Just describe what you want!")

# --- Step 1: API Key Input ---
api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

# --- Step 2: Prompt Input ---
user_prompt = st.text_area("✍️ Describe what you want the prompt to do", height=200)

# --- Step 3: Submit ---
if st.button("✨ Enhance Prompt"):

    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not user_prompt.strip():
        st.error("Please enter a prompt to enhance.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model="gpt-4",  # or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": (
                        "You are a helpful prompt generator. "
                        "Rewrite the user's prompt to make it more clear, specific, and effective. "
                        "Do not respond to the prompt. Only return the improved prompt."
                    )},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7
            )

            improved_prompt = response.choices[0].message.content
            st.success("✅ Prompt Enhanced Successfully!")
            st.text_area("🪄 Improved Prompt", improved_prompt, height=200)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
