import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
import os
import time

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
model = ChatOpenAI(
    model = "deepseek/deepseek-chat-v3.1:free",
    openai_api_key = api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.8
)
# chat_history = {}

# # There's a issue here that after some prompt it will be __.
# while True:
#     user_input = input("You: ").strip().lower()
#     chat_history.append(user_input)
#     if user_input == "exit":
#         break
#     response = model.invoke(chat_history)
#     print(f"AI: {response.content}")
#     chat_history.append(response.content)
  
# # Now we are doing it in a more systematic approach
 
# while True:
#     user_input = input("You: ").format().strip()
#     chat_history.append({"User":user_input})
#     if user_input == "exit":
#         break
#     response = model.invoke(chat_history)
#     print(f"AI: {response.content}")
#     chat_history.append({"Ai":response.content})
  
# #The above code is enhanced by the langchain by using messages

# messages = [
#     SystemMessage("you are a assistant and please do not think turn off your thinking abilities")
# ]
 
# while True:
#     user_input = input("You: ").format().strip()
#     if user_input == "exit":
#         print(messages)
#         break
#     messages.append(HumanMessage(content=user_input))
#     response = model.invoke(messages)
#     print(f"AI: {response.content}")
#     messages.append(AIMessage(content = response.content))
    
# Dynamic chat prompt template

# You will notice a wierd syntax here that might be confusing 

topic = input("Please provide the topic: ").lower()
domain = input('Please provide the domain: ').lower()
chat_template = ChatPromptTemplate([
    ('human', 'expalin this {topic} in simple terms'),
    ('system','you are a helpful ai summariser and an expert of this {domain}')
]) 

prompt = chat_template.invoke({'topic':topic, 'domain':domain})
print(prompt)
response = model.invoke(prompt) 
print(response.content)