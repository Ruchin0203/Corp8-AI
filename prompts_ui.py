from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Tool")
user_input = st.text_input("Enetr your prompt")

if st.button("summarise"):
    result = model.invoke(user_input)
    st.write("some random text")