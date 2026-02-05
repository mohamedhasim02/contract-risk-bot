import os
from openai import OpenAI

def explain_clause(text: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "⚠️ OpenAI API key not found. Please set OPENAI_API_KEY in Streamlit Secrets."

    client = OpenAI(api_key=api_key)

    prompt = f"""
Explain the legal risk in simple terms and suggest improvement:

Clause:
{text}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        temperature=0.3,
        max_output_tokens=200
    )

    return response.output_text
