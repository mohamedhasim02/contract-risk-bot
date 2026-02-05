
def assess_clause_risk(text):
    t=text.lower()
    score=1
    if "indemnify" in t or "penalty" in t or "non-compete" in t:
        score=3
    elif "terminate" in t or "auto-renew" in t:
        score=2
    risk={1:"Low",2:"Medium",3:"High"}[score]
    return risk, score

def overall_risk(clauses):
    return round(sum(c["score"] for c in clauses)/len(clauses),2)
