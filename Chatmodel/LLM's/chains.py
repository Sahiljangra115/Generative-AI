from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain.schema.runnable import RunnableParallel
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
    model = "deepseek/deepseek-chat-v3.1:free",  
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1"    
)

# prompt = PromptTemplate(
#     template="Give me a 5 point summary of the {topic}",
#     input_variables=['topic']
# )
user_input = input("Please provide a topic: ")
# parser = StrOutputParser()

# chain = prompt | model | parser
# chain.get_graph().print_ascii()

# print(chain.invoke({'topic': user_input}))


# Parallel chains
parser = StrOutputParser()
openai_base_url = "https://openrouter.ai/api/v1"

llm = ChatOpenAI(
    openai_api_key=api_key,
    openai_api_base=openai_base_url,
    model="moonshotai/kimi-k2:free",
)

prompt1 = PromptTemplate(
    template = "Give me some brief notes for the {topic} ",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template = "Give me some quiz questions for the {topic} ",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template = "Give me the merge of both {notes} and {quiz} ",
    input_variables=["notes", "quiz"]
)

chain1 = prompt1 | model | parser
chain2 = prompt2 | llm | parser
parallel_chain = RunnableParallel(
{
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | llm | parser
}
)

merger_chain = prompt3 | model | parser
final_chain = parallel_chain | merger_chain

final_result = final_chain.invoke({'topic': user_input})
print(final_result)