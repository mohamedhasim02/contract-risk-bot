
import streamlit as st
from core.text_extraction import extract_text
from core.language_handler import detect_language
from core.contract_classifier import classify_contract
from core.clause_extractor import extract_clauses
from core.intent_detector import detect_intent
from core.risk_engine import assess_clause_risk, overall_risk
from core.compliance_engine import check_compliance
from core.llm_reasoning import explain_clause
from core.report_generator import generate_pdf
import json, datetime, os

st.title("📄 Contract Analysis & Risk Assessment Bot")

file = st.file_uploader("Upload Contract", type=["pdf","docx","txt"])

if file:
    text = extract_text(file)
    lang = detect_language(text)
    ctype = classify_contract(text)

    st.success(f"Language: {lang}")
    st.info(f"Contract Type: {ctype}")

    clauses = extract_clauses(text)

    for c in clauses:
        c["intent"] = detect_intent(c["text"])
        c["risk"], c["score"] = assess_clause_risk(c["text"])

    risk_score = overall_risk(clauses)
    st.metric("Overall Risk Score", risk_score)

    for c in clauses:
        st.subheader(c["clause_id"])
        st.write(c["text"])
        st.warning(f"Risk: {c['risk']} | Intent: {c['intent']}")

        if c["risk"] != "Low":
            with st.expander("Explain & Improve"):
                st.write(explain_clause(c["text"]))

    issues = check_compliance(text)
    if issues:
        st.error("Compliance Issues")
        for i in issues:
            st.write(i)

    if st.button("Generate PDF Report"):
        os.makedirs("reports", exist_ok=True)
        summary = f"Contract: {ctype}\nRisk Score: {risk_score}\nIssues:\n" + "\n".join(issues)
        generate_pdf(summary, "reports/contract_report.pdf")
        st.success("PDF Generated")

    os.makedirs("data/audit_logs", exist_ok=True)
    with open(f"data/audit_logs/{datetime.datetime.now().isoformat()}.json","w") as f:
        json.dump({"file":file.name,"risk":risk_score},f)
