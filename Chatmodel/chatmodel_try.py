from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv  
import os

# load_dotenv()
# #trying git
api_key = os.getenv("OPENROUTER_API_KEY")

# openai_base_url = "https://openrouter.ai/api/v1"

# # models = ChatOpenAI(
# models = OpenAIEmbeddings(
#     openai_api_key=api_key,
#     openai_api_base=openai_base_url,
#     # model="moonshotai/kimi-k2:free",
#     model="google/gemma-3n-e2b-it:free",
#     dimensions=32,                         # Optional: Set temperature for response variability
# )

# # Try a simple message
# response = models.embed_query("where is india")
# # print(response)                           # gives raw output 
# print(str(response))                     # gives content of the response



from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
#   api_key="<OPENROUTER_API_KEY>",
api_key = os.getenv("OPENROUTER_API_KEY")
)

completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },
  extra_body={},
  model="google/gemma-3n-e2b-it:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)



