# Integreting our code with OPENAI API

# ================Importing Library===============#
import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
from langchain.llms import Ollama
# ================================================#

# ===========Initializing the llm model===========#
# os.environ['OPENAI_API_KEY']=openai_key

llm = Ollama(
    model='qwen'
)

#=================================================#

# ===============Streamlit Framework==============#
st.title('Langchain Demo With Qwen Model')
input_text = st.text_input("Ask Anything Here")

if input_text:
    st.write(llm(input_text))

#=================================================#