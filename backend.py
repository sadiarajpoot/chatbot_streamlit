import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def get_text_output(input_text):
    response = co.chat(
        model="command-r7b-12-2024",
        message=input_text
    )
    return response.text
