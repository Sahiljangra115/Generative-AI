from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

tavily_search = TavilySearchResults(max_results=3)
search_docs = tavily_search.invoke("What is LangGraph?")
llm = ChatOpenAI(model="deepseek/deepseek-chat-v3.1:free",api_key=api_key, openai_api_base="https://openrouter.ai/api/v1")

print(search_docs)
response = llm.invoke(f"Please provide a concise summary of the following information  {search_docs}")
print('\n', response.content)