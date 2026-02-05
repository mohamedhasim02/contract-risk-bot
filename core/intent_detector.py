
def detect_intent(text):
    t=text.lower()
    if "shall not" in t: return "Prohibition"
    if "shall" in t or "must" in t: return "Obligation"
    if "may" in t: return "Right"
    return "Neutral"
