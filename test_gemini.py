from google import genai

client = genai.Client(api_key="AIzaSyAnfUI7RxjM1lPPJOVRzQro0bfA7PCcEHM")
response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="hey how are you."
)
print(response.text)
