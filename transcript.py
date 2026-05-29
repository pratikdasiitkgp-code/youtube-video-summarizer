from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_transcript(audio_file):

    with open(audio_file, "rb") as file:

        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=file
        )

    return transcript.text