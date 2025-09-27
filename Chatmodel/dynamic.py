import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
import time

# Load environment variables
load_dotenv()

st.title("Hello From Sahil")
st.subheader("Generative AI Learners")
st.text("Welcome to your interactive platform for AI Learning")
# st.sidebar.write("choose your favourite model")

models = st.sidebar.selectbox(" Choose your favourite Model", ["ChatGPT", "Gemini", "Claude", "Qwen", "Other"])

if models:
    match models:
        case "ChatGPT":
            api_key = os.getenv("OPENROUTER_API_KEY")
            
        case "Gemini":
            api_key = os.getenv("OPENROUTER_API_KEY")
          
        case "Claude":
            api_key = os.getenv("OPENROUTER_API_KEY")
            
        case "Qwen":
            api_key = os.getenv("OPENROUTER_API_KEY")
        case "Other":
            api_key = os.getenv("OPENROUTER_API_KEY")
        case _:
            api_key = None
    
    # Display the selected model and API key status with toast notifications
    if api_key:
        st.toast(f"{models} API key loaded successfully!", icon="✅")
        time.sleep(3)
        st.empty()
    else:
        st.toast(f"No API key found for {models}. Please check your .env file.", icon="⚠️")

temperature = st.sidebar.slider("Temperature", min_value=0.1, max_value=1.0, step=0.1)
k = st.sidebar.slider("K", min_value=0.1, max_value=1.0, step=0.1)
p = st.sidebar.slider("p", min_value=0.1, max_value=1.0, step=0.1)

# st.subheader("Please provide your prompt/question")
# st.text("This section is for static prompt")
# st.text("This section is for dynamic prompt")

dynamic_prompt = st.chat_input("What's your question")


# Only process if user entered a prompt
if dynamic_prompt:
    # Display user message
    st.chat_message("user").write(dynamic_prompt)
    
    # Initialize the model based on selected option
    if models and api_key:
        try:
            # Create ChatOpenAI instance for OpenRouter (works with Qwen and other models)
            model = ChatOpenAI(
                model="deepseek/deepseek-chat-v3.1:free",  # Use the selected model
                openai_api_key=api_key,
                openai_api_base="https://openrouter.ai/api/v1",
                temperature=temperature
            )
            
            # Get response from the model
            with st.spinner(f"Getting response from {models}..."):
                response = model.invoke(dynamic_prompt)
            
            # Display assistant response
            st.chat_message("assistant").write(response.content)
            
        except Exception as e:
            st.error(f"Error calling {models}: {str(e)}")
    else:
        st.warning("Please select a model and ensure API key is configured.")


