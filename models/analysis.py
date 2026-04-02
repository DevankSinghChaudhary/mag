from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv("NVIDIA_API_KEY")
)
def call_analysis(prompt):
    completion = client.chat.completions.create(
      model="deepseek-ai/deepseek-v3.2",
      messages=[{"role":"user","content":prompt}],
      temperature=1,
      top_p=0.95,
      max_tokens=2000,
      stream=False
    )
    return completion.choices[0].message.content

def new_model(prompt):
  response = client.responses.create(
    model="openai/gpt-oss-120b",
    input=prompt,
    max_output_tokens=4096,
    top_p=1,
    temperature=1,
    stream=True
  )