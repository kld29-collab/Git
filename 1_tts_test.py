import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

# Set up the request
url = "https://api.openai.com/v1/audio/speech"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "tts-1",
    "input": "Hello, this is a test of OpenAI's text-to-speech API.",
    "voice": "alloy"
}

# Make the request
response = requests.post(url, headers=headers, json=data)

if response.status_code != 200:
    print(f"Error: {response.status_code} - {response.text}")
    exit(1)

# Save the audio content as an MP3 file
with open("output.mp3", "wb") as f:
    f.write(response.content)

print("Audio saved as output.mp3")