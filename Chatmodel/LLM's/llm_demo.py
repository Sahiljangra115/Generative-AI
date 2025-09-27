from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
#trying git
api_key = os.getenv("OPENROUTER_API_KEY")

# Set the base URL for OpenRouter
openai_base_url = "https://openrouter.ai/api/v1"

# Initialize the chat mmodel = ""odel
llm = ChatOpenAI(
    openai_api_key=api_key,
    openai_api_base=openai_base_url,
    model="moonshotai/kimi-k2:free",
)

# Try a simple message
response = llm.invoke("What is my name")
print(response.content)
