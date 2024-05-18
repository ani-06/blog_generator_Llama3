#Importing necessary packages:

import streamlit as st
from langchain_community.llms import Ollama

#Function for getting response from Llama3 Model using Ollama:

def responsefromllama3(blog_title,words,purpose):

    llm = Ollama(model='llama3',temperature=0.4,)
    response = llm.invoke(f"Write a blog about {blog_title} in {words} words for {purpose}")
    return response

#Creating user interface using Streamlit:

st.set_page_config(page_title='Blog Generator',page_icon='🚀',
                   layout="centered",initial_sidebar_state="collapsed")

st.header('GENERATE YOUR BLOG HERE !📔',anchor=False,
          help="This is Simple Blog generator using Meta Llama-3 LLM model",divider='blue')

#Creating columns:

blog,no_of_words,needs = st.columns([7,3,4])

with blog:
    blog_title = st.text_input("Blog is all about?")

with no_of_words:
    words = st.text_input("Words to be present:")

with needs:
    purpose = st.selectbox("Writing for",("Developers","Research","School","College"))
    
submit = st.button("Generate")

#Getting response from Llama3:
    
if submit:
    if not blog_title:
        st.write("Please fill Blog Title")
    elif not words:
        st.write("Please fill no.of.words to be in blog")
    else:
        st.write(f"Your blog about {blog_title}is here!!",responsefromllama3(blog_title,words,purpose))