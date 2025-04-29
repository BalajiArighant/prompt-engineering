import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000/evaluate")

st.title("Prompt Scoring Playground 🎯")

prompt_input = st.text_area("Enter your prompt here:", height=200)

if st.button("Evaluate Prompt"):
    if prompt_input.strip():
        with st.spinner('Evaluating...'):
            res = requests.post(API_URL, json={"prompt": prompt_input})
            if res.status_code == 200:
                result = res.json()
                st.success(f"Score: {result['score']}/10")
                if result['feedback']:
                    st.subheader("Feedback")
                    # for fb in result['feedback']:
                    #     st.write(f"- {fb}")
                    st.write(result["feedback"])
                st.subheader("AI's Response")
                st.code(result['ai_response'])
            else:
                st.error("Failed to evaluate the prompt.")
    else:
        st.warning("Please enter a prompt first.")