from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(model="mistralai/mistral-small-3.2-24b-instruct:free",api_key=api_key, openai_api_base="https://openrouter.ai/api/v1")

def add(a: int, b: int) -> int:
    return a + b
def subtract(a: int, b: int) -> int:
    return a - b
def multiply(a: int, b: int) -> int:
    return a * b
def divide(a: int, b: int) -> float:
    if b == 0:
        return "Error: Division by zero"
    return a / b

tools = [add, subtract, multiply, divide]
llm_with_tools = llm.bind_tools(tools)
response = llm_with_tools.invoke("What is 5 plus 3?")
print(response.content)