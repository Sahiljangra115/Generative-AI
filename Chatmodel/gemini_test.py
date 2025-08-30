from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-pro",
    google_api_key  = os.environ.get("GOOGLE_API_KEY")
)
response = llm.invoke("Hello, what's up!")
print(response.content)