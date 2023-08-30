import os
import streamlit as st
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = openai_key

# SINGLE PORMPT SEARCH ENGINE

st.title("Celebrity Search Engine")
input_text = st.text_input("Search Here...")

# Prompt Template
first_input_prompt = PromptTemplate(input_variables = ['name'],
                                    template = "Tell me about {name}")

# OPENAI LLM
llm = OpenAI(temperature = 0.8)
chain = LLMChain(llm = llm, prompt = first_input_prompt, verbose = True)

if input_text:
    st.write(chain.run(input_text))
