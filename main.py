from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


##prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant.Please respond to to the user queries"),
        ("user", "Question:{question}")
    ]
)

st.title("LangChain Google GenAI")
input_text = st.text_input("Enter your Question")

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")
outpu_parser= StrOutputParser()
chain= prompt | llm | outpu_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)



# response=llm.invoke("hello")
# print(response.content)