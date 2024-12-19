# Creating a Security Test Report Template
security_test_report = {
    "Vulnerability ID": ["SEC001", "SEC002", "SEC003"],
    "Area": ["Login", "Payment API", "User Profile"],
    "Description": [
        "Weak password policy",
        "Sensitive data exposed in payload",
        "Stored XSS on profile description"
    ],
    "Severity": ["High", "Critical", "Medium"],
    "Recommendation": [
        "Enforce strong passwords with regex validation.",
        "Use encryption (HTTPS, TLS 1.2+).",
        "Sanitize user input on all fields."
    ]
}

security_report_df = pd.DataFrame(security_test_report)

# Save Excel file
file_path = "/mnt/data/Security_Test_Report.xlsx"

with pd.ExcelWriter(file_path) as writer:
    security_report_df.to_excel(writer, index=False, sheet_name="Security Report")
