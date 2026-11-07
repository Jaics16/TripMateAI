import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env")

MODEL = "gemini-3.5-flash-lite"

client = genai.Client(api_key=API_KEY)

print(f"Testing model: {MODEL}")

try:
    response = client.models.generate_content(
        model=MODEL,
        contents="Introduce yourself as a Kerala travel assistant in one sentence."
    )

    print("\nSUCCESS! Gemini is responding.")
    print(response.text)

except Exception as error:
    print("\nMODEL TEST FAILED")
    print(type(error).__name__)
    print(error)