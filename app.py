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

file = st.file_uploader("Upload Contract", type=["pdf", "docx", "txt"])

# EVERYTHING BELOW MUST BE INSIDE THIS BLOCK
if file:
    text = extract_text(file)
    lang = detect_language(text)
    contract_type = classify_contract(text)

    st.success(f"Language: {lang}")
    st.info(f"Contract Type: {contract_type}")

    clauses = extract_clauses(text)

    for clause in clauses:
    clause["intent"] = detect_intent(clause["text"])

    risk_result = assess_clause_risk(clause["text"])
    clause["risk"] = risk_result["level"]
    clause["score"] = risk_result["score"]

    risk_score = overall_risk(clauses)
    st.metric("Overall Risk Score", risk_score)

    for c in clauses:
        st.subheader(c["clause_id"])
        st.write(c["text"])
        st.warning(f"Risk: {c['risk']} | Intent: {c['intent']}")

        if c["risk"] != "Low":
            with st.expander("Explain & Improve"):
                st.write(explain_clause(c["text"]))

    compliance = check_compliance(text)
    if compliance:
        st.error("Compliance Issues")
        for issue in compliance:
            st.write(issue)

    # ✅ PDF SECTION (CORRECT PLACE)
    if st.button("Generate PDF Report"):
        pdf_path = "reports/contract_report.pdf"

        summary = (
            f"Contract Type: {contract_type}\n"
            f"Overall Risk Score: {risk_score}\n\n"
            "Compliance Issues:\n"
            + ("\n".join(compliance) if compliance else "None")
        )

        generate_pdf(summary, pdf_path)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Download PDF Report",
                data=f,
                file_name="contract_report.pdf",
                mime="application/pdf"
            )

    # Audit Log
    os.makedirs("data/audit_logs", exist_ok=True)
    with open(f"data/audit_logs/{datetime.datetime.now().isoformat()}.json", "w") as f:
        json.dump({"file": file.name, "risk": risk_score}, f)
