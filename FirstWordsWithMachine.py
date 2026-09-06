from google import genai
from google.genai import types

# 1. API key passed directly to the client
client = genai.Client(api_key="AQ.Ab8RN6LLhxQ_0JPOo6i8X6a_J-MMMoxdmcuhaReSe-F702Xu6A")

RULES = """You are a homework coach.
Explain step by step.
NEVER give the final answer."""

question = input("Ask me anything: ")

# 2. Model passed inside the function call
reply = client.models.generate_content(
    model="gemini-3.1-flash-lite",  # Gemini Free-Tier Model
    contents=question,
    config=types.GenerateContentConfig(
        system_instruction=RULES,
        max_output_tokens=500,
    ),
)

print(reply.text)