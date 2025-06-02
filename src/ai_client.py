from together import Together
from dotenv import load_dotenv
from utils.prompt import promptToAi
import os

load_dotenv()

TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')

client = Together()
client.api_key = TOGETHER_API_KEY

def askAi(language,model_attributes):
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[
            {
                "role": "user",
                "content": promptToAi(language=language,model_attributes=model_attributes)
            }
        ]
    )
    return response.choices[0].message.content
