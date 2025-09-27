from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
    model = "deepseek/deepseek-chat-v3.1:free",  # Use the selected model
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1"
)
user_input = input("Please provide a topic: ")
parser1 = JsonOutputParser()
parser = StrOutputParser()

#1st prompt 
template1 = PromptTemplate(                # prompt template is used for dynamic prompting it's getting 2 attributes here (template, input_variable)
    template = "You are a reseaarch assistant . you have to give detailed report on this {topic}",
    input_variables= ['topic']
)
template2 = PromptTemplate(                # prompt template is used for dynamic prompting it's 2 attributes here (template, input_variable)
    template = "You are a Summariser assistant . you have to give summarise this {text} in 5 line",
    input_variables= ['text']
)

# 3rd prompt 
template3 = PromptTemplate(
    template = 'Write the story of john wick movie with keanu reeves details as an actor. {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions': parser1.get_format_instructions()} 
)

# prompt1 = template1.invoke({'topic':user_input})
# report = model.invoke(prompt1)
# prompt2 = template2.invoke({"text":report.content})
# result = model.invoke(prompt2)
# print(result.content)

# Stroutputparser
# chain = template1 | model | parser | template2 | model | parser

# Json output parser
chain1 = template3 | model | parser1
print(chain1.invoke({}))
# print(chain.invoke(user_input))