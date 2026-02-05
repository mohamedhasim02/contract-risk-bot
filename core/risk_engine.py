def assess_clause_risk(text):
    text = text.lower()

    if "penalty" in text or "termination" in text or "liability" in text:
        return {"level": "High", "score": 8}
    elif "notice" in text or "renewal" in text:
        return {"level": "Medium", "score": 5}
    else:
        return {"level": "Low", "score": 2}


def overall_risk(clauses):
    if not clauses:
        return 0

    total = sum(c.get("score", 0) for c in clauses)
    return round(total / len(clauses), 2)
