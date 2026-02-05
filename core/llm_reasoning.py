
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_clause(clause):
    prompt=f"Explain this clause simply and suggest safer wording:\n{clause}"
    r=openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        temperature=0.3
    )
    return r.choices[0].message.content
