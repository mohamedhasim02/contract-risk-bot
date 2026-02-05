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
