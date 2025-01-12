from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()



## Langsmith tracking call
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]= "true"

## creating chatbot
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assisstant. Please provide response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
    }
    .input-box {
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
        border: 2px solid #4CAF50;
        width: 100%;
        box-sizing: border-box;
        margin-top: 20px;
    }
    .input-box:focus {
        border-color: #4CAF50;
        box-shadow: 0 0 5px #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Display a more attractive title
st.markdown('<h1 class="title">Langchain Demo with Qwen2 API</h1>', unsafe_allow_html=True)

# Create a more appealing input box
input_text = st.text_input("Ask anything about your topic", key="user_input", 
                           placeholder="Enter your question here...",
                           help="Type your question related to the topic")

# Add some spacing and other UI elements if needed
st.markdown("<hr>", unsafe_allow_html=True)
st.text("Model response:")

## openai LLM call
llm=Ollama(model="qwen2:0.5b")
output_parser = StrOutputParser()

## chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

# print('Hello')