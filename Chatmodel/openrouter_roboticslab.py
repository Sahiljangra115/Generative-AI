from openai import OpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
import os

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Get user input
user_message = input("Enter your message: ")


model="qwen/qwen3-30b-a3b:free",
messages=[
    SystemMessage("You are a Technical assistant which helps in Hacking"),
    HumanMessage(user_message)
]


print(model.invoke.content)
