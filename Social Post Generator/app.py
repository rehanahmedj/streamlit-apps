# app.py

import streamlit as st
from openai import OpenAI

# --- Page Config ---
st.set_page_config(page_title="Social Media Post Generator", layout="centered")
st.title("📱 Social Media Post Generator")
st.write("Enter an idea and get 3 ready-to-use social media posts!")

# --- API Key Input ---
api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

# --- Idea Input ---
idea = st.text_area("💡 What's the post about?", height=200)

# --- Generate Button ---
if st.button("✍️ Generate Posts"):

    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not idea.strip():
        st.error("Please enter an idea to generate posts.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            prompt = (
                f"Create 3 distinct social media posts based on the idea below:\n"
                f"---\n"
                f"Idea: {idea}\n"
                f"---\n"
                f"1. A **WhatsApp message** (casual, friendly)\n"
                f"2. A **LinkedIn post** (professional, thoughtful)\n"
                f"3. A **Twitter/X post** (concise, impactful)"
            )

            response = client.chat.completions.create(
                model="gpt-4",  # or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": (
                        "You are a helpful assistant who writes in different tones for social platforms. "
                        "Do not invent the topic — only write the 3 posts as requested."
                    )},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            output = response.choices[0].message.content

            # Split output into parts based on bullet markers
            sections = output.split('\n\n')
            for section in sections:
                if section.lower().startswith("1"):
                    st.subheader("🟢 WhatsApp")
                elif section.lower().startswith("2"):
                    st.subheader("🔵 LinkedIn")
                elif section.lower().startswith("3"):
                    st.subheader("🔷 Twitter/X")
                st.write(section.strip())

        except Exception as e:
            st.error(f"Something went wrong: {e}")
