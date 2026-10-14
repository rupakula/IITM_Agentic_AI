import os
import sys
from dotenv import load_dotenv
from google import genai

# Load GEMINI_API_KEY from the environment — never hard-code keys
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask(question):
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=[
            "You are concise.\n\n"
            f"User question: {question}"
        ],
    )

    return response.text


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "Say hello."
    print(ask(q))
