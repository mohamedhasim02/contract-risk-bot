
def check_compliance(text):
    issues=[]
    t=text.lower()
    if "jurisdiction" not in t:
        issues.append("Jurisdiction clause missing")
    if "non-compete" in t:
        issues.append("Non-compete may be unenforceable in India")
    return issues
