import streamlit as st
from openai import OpenAI
import json
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
    question_quantity = st.number_input("How many questions would you like in your quiz?", min_value = 3, max_value = 30, value = 10)
    method = st.selectbox(
        "How would you like your quiz?",
        [
            "multiple choice",
            "short answer",
        ]
    )

    if method == "multiple choice":
        system_prompt = f""" Make this response in json with {question_quantity} questions""" + """
        [
            { "text of first question" : [ "choice", "choice", "choice", "choice"]},
            { "text of second question" : [ "choice", "choice", "choice", "choice"]}
        ]
        """
        assistant_prompt = f"Imagine you are teaching at {level}. Make sure that one of the choices provided is the correct answer."
        user_prompt = subject
    if method == "short answer":
        system_prompt = f"""Create a short answer quiz in json with {question_quantity} questions.""" + """
        Format the JSON like this:
        [
            { "Question" : "Explain"},
            { "Question" : "Explain"}
        ]
        
        Make sure that if the topic is a Math subject, give math problems."""
        assistant_prompt = f"Teach this topic to a {level} student."
        user_prompt = subject
    # system_prompt = f'''
    # Give me a response in json:
    # {}
    # '''
    # assistant_prompt = ""
    # user_prompt = ""
    
if style == "Explain a concept":
    method = st.selectbox(
        "How would you like me to explain your concept",
        [
           "simple explanation",
            "detailed explanation",
            "step-by-step explanation"
        ]
    )
    system_prompt = f"You are to make a {method}."
    assistant_prompt = f"Explain this topic at {level}."
    user_prompt = subject

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
    ai_response= response.choices[0].message.content
    if style != "Quiz you":
        st.write(ai_response)
    else:
        quiz = json.loads(ai_response)
        st.write("###  Your Quiz")

        if method == "multiple choice":
            formatted_quiz = ""
            for qa_set in quiz:
                question = list(qa_set)[0]
                answer = qa_set[question] 
                formatted_quiz += "\n**" + question + "**\n"
                for a in answer:
                    formatted_quiz += f"- {a}\n"
            st.markdown(formatted_quiz)

        if method == "short answer":
            for qa_set in quiz:
                question = "### " + qa_set["Question"] 
                st.write(question)




            # formatted_quiz = "" 
            # for i, qa_set in list(quiz):
            #     question_text = qa_set["Question"]
            #     formatted_quiz += f"\n\n## Question {i+1}\n"
            #     formatted_quiz += f"**{question_text}**\n\n"
            #     formatted_quiz += "> Write your answer below.\n"
            # st.markdown(formatted_quiz)


            