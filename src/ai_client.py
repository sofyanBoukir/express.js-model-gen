from together import Together
from dotenv import load_dotenv
import os

load_dotenv()

TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')

client = Together()
client.api_key = TOGETHER_API_KEY

def askAi(language,models):
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[
            {
                "role": "user",
                "content": "What are some fun things to do in New York?"
            }
        ]
    )
    return response.choices[0].message.content
