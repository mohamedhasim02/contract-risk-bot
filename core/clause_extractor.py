
import re
def extract_clauses(text):
    chunks=re.split(r"\n(?=\d+\.)",text)
    return [{"clause_id":f"C{i+1}","text":c.strip()} for i,c in enumerate(chunks)]
