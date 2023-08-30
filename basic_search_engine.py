import os
import streamlit as st
from constants import openai_key
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = openai_key

st.title("Search Engine")
input_text = st.text_input("Search Here...")

llm = OpenAI(temperature = 0.8)

if input_text:
    st.write(llm(input_text))
