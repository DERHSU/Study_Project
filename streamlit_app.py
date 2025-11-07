import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key = st.secrets["api_key"]
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
        "College or beyond",
    ]
)
if style == "Summarize a topic":
    method = st.selectbox(
        "How would you like your summary?",
        [
           "short summary",
            "detailed summary",
            "bullet-point summary",
        ]
    )

    # Prompts for summary
    system_prompt = f"You are to produce a {method}. "
    assistant_prompt = f"Explain this to a student at {level}"
    user_prompt = subject


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
    
    # 4
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "assistant", "content": assistant_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    st.write(response.choices[0].message.content)