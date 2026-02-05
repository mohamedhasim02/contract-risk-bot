import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_clause(clause):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"""
Explain the following contract clause in simple business English.
Identify risks and suggest a safer alternative.

Clause:
{clause}
"""
        )

        return response.output_text

    except Exception as e:
        return (
            "⚠️ AI explanation temporarily unavailable.\n\n"
            "Manual Risk Insight:\n"
            "- This clause may impose obligations or restrictions.\n"
            "- Consider negotiating clearer limits, duration, or liability caps.\n"
            "- Consult a legal expert before signing."
        )
