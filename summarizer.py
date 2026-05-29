from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def summarize_text(text):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": f"""
                Summarize this transcript.

                Give:
                1. Overview
                2. Key Points
                3. Action Items

                Transcript:
                {text}
                """
            }
        ]
    )

    return response.choices[0].message.content