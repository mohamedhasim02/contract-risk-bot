from openai import OpenAI
import os

def explain_clause(text):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "⚠️ OpenAI API key not configured. Please set OPENAI_API_KEY in Streamlit Secrets."

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
You are a legal assistant.
Explain the risk in this clause in simple terms and suggest an improvement.

Clause:
{text}
"""
    )

    return response.output_text
