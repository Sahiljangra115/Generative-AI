# There are 4 types of documents loaders
# 1. TextLoader
# 2. PyPDFLoader
# 3 WebBaseLoaders
# 4 CSVLoader
from langchain_community.document_loaders import TextLoader, PyPDFLoader, WebBaseLoader, CSVLoader
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

from openai import api_key

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

prompt1 = PromptTemplate(
    template = "Give me some brief notes for the {topic} ",
    input_variables=["topic"]
)

model = ChatOpenAI(
    model = "deepseek/deepseek-chat-v3.1:free",  
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1"    
)
# --> textloader for text files

loader = TextLoader('assets/poem.txt', encoding = 'utf-8')
data = loader.load()

# --> PyPDFLoader for pdf files

# not great for image pdf it's good for text pdf
# Note: text-encoding.pdf is not a valid PDF file, commenting out for now
# loader1 = PyPDFLoader('assets/text-encoding.pdf')
# data1 = loader1.load()


# print(type(data))
# print(len(data))
# print(data[0].page_content)
parser = StrOutputParser()
chain = prompt1 | model | parser
print(chain.invoke({'topic': data[0].page_content}))
# print(chain.invoke({'topic': data1[0].page_content}))