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

# Read narration text from file
with open("narration.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

async def main():
    client = AsyncOpenAI(api_key=api_key)
    for line in lines:
        print(f"Narrating: {line}")
        # Get TTS audio (not streaming, but works reliably)
        response = await client.audio.speech.create(
            model="tts-1",
            input=line,
            voice="alloy",
            response_format="mp3"
        )
        # Save to a temporary file and play
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            tmp.write(response.content)
            tmp.flush()
            os.system(f'afplay "{tmp.name}"')

if __name__ == "__main__":
    asyncio.run(main())
