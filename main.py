from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
load_dotenv()



llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001")
response=llm.invoke("I want you to create an weather app that shows the current weather in my city. The app should be simple and user-friendly. Use HTML, CSS, javascript to make 3 seperate files and you should be able  store it in my system. If you are unable to create the files and store them by your own then say what are the tools that are required to make the files and store them lets say you might require Linux based commands to make directory and files how about that.")
print(response.content)