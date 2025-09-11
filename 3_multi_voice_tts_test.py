import os
import asyncio
import tempfile
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

# List of OpenAI voices (as of 2024)
voices = [
    "alloy",
    "echo",
    "fable",
    "onyx",
    "nova",
    "shimmer"
]

# Example effects to try (simulate by changing text or voice)
effects = [
    {"desc": "Normal narration.", "text": "This is a normal voice."},
    {"desc": "Excited!", "text": "Wow! This is so exciting!"},
    {"desc": "Questioning", "text": "Is this really working?"},
    {"desc": "Slow and dramatic", "text": "Let us... slow... things... down..."},
    {"desc": "Robot style", "text": "Beep boop. I am a robot. 01101000."}
]

async def main():
    client = AsyncOpenAI(api_key=api_key)
    for voice in voices:
        print(f"\n--- Voice: {voice} ---")
        for effect in effects:
            print(f"Effect: {effect['desc']}")
            response = await client.audio.speech.create(
                model="tts-1",
                input=effect["text"],
                voice=voice,
                response_format="mp3"
            )
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                tmp.write(response.content)
                tmp.flush()
                print(f"Playing: {effect['desc']} with {voice}")
                os.system(f'afplay "{tmp.name}"')

if __name__ == "__main__":
    asyncio.run(main())
