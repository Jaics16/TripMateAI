
import os

from dotenv import load_dotenv
from google import genai

# Load API configuration
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

if not API_KEY or API_KEY == "PASTE_YOUR_API_KEY_HERE":
    raise ValueError(
        "Please add your actual Gemini API key to .env"
    )

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Send a test question
response = client.models.generate_content(
    model=MODEL,
    contents="Introduce yourself as a Kerala travel assistant in one sentence."
)

print("\nGemini connection successful!")
print(response.text)
