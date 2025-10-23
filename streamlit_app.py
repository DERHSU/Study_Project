import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key = "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"
)
subject = st.text_input("What subject would you like to study?")
style = st.selectbox(
    "How would you like me to assist your studies?",
    [
        "Summarize a topic",
        "Quiz you",
        "Explain a concept"
    ]
)
level = st.selectbox(
    "Select a level",
    [
        "Elementary level",
        "Middle school level",
        "High School level",
        "Colledge or beyond",
    ]
)
if style == "Summarize a topic":
    method = st.selectbox(
        "How would you like your summary?",
        [
           "short summary",
            "detailed summary",
            "bullet-point format",
            "formal",
            "casual"
        ]
    )
if style == "Quiz you":
    method = st.selectbox(
        "How would you like your quiz?",
        [
           "10 questions",
            "20 questions",
            "multiple choice",
            "short answer",
            "easy",
            "hard"
        ]
    )
if style == "Explain a concept":
    method = st.selectbox(
        "How would you like me to explain your concept",
        [
           "simple explanation",
            "detailed explanation",
            "step-by-step explanation"
        ]
    )
run = st.button("Submit your request")
assistant_message = "You're supposed to be the best study tool for students"
if run:
    user_prompt = f""
    # 4
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": content_message},
            {"role": "assistant", "content": assistant_message},
            {"role": "user", "content": user_prompt}
        ]
    )
    st.write(response.choices[0].message.content)