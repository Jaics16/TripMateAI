import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=API_KEY)

print("\nChecking models available to your API key...\n")

try:
    for model in client.models.list():
        if "generateContent" in (model.supported_actions or []):
            print(model.name)

except Exception as error:
    print("\nUnable to list models:")
    print(error)