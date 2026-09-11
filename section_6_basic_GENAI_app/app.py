import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]="true"

from langchain_ollama import ChatOllama
import streamlit as st


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# prompt template;

prompt = ChatPromptTemplate([
    ("system", "Respond to user as per question with random mewing and a ASCII based art "),
    ("user","{question}"),
])

st.title("Langchain Demo")
st.write("Model: mannix/llama3.1-8b-abliterated:q4_k_m")

input_text = st.text_input("Your question:")

llm = ChatOllama(model="mannix/llama3.1-8b-abliterated:q4_k_m")

output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    st.write(
        chain.invoke({"question":input_text})
    )


# mannix/llama3.1-8b-abliterated:q4_k_m