#Write a simple app that reads the user input and display the output
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
openai.api_key = st.secrets["API_key"]

import openai
import os

def summarize(input_string): 
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt= input_string +"\n",
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        temperature=0.0,
        stop=None,
    )
    answer = response.choices[0].text.strip()
    return answer

# Define the Streamlit app
def app():
    st.header("Welcome to atyourLevel")
    st.subheader("Louie F. Cervantes M. Eng. \n(c) 2023 WVSU College of ICT")
    
    st.title("atyourLevel is a topic summarizer")
    st.write("This app uses the openAI davinci-gpt3 engine to generate age appropriate summary of any complex topic.")
    st.write("To try an example, copy paste the sample topic beloe into the input box.  You can also come up with you own set of instructions.")
    st.write("Example topic:")
    st.write("ChatGPT is a large language model developed by OpenAI based on the GPT-3 architecture. It has been trained on a massive amount of text data using unsupervised learning techniques to generate human-like responses to text-based prompts. ChatGPT is capable of performing a wide range of natural language processing tasks such as text completion, question-answering, summarization, translation, and more. It has the ability to understand context, recognize patterns, and generate coherent and relevant responses to a variety of inputs. ChatGPT is designed to improve its performance with more training data and can adapt to different tasks and domains with fine-tuning.")
    
    level = 'kinder'
    options = ['kinder', 'elementary', 'high school', 'senior high', 'college', 'graduate school', 'post-graduate']
    selected_option = st.selectbox('Select the level of the user', options)
    if selected_option=='kinder':
        language = selected_option
    else:
         language = selected_option
             
    # Create a multiline text field
    user_input = st.text_area('Paste the instructions in this box', height=10)
    
             
    # Display the text when the user submits the form
    if st.button('Submit')::
        output = summarize("Generate a summary appropriate for the mental level of " + level + " of the topic " + user_input)
        st.write(output)

# Run the app
if __name__ == "__main__":
    app()
