import pandas as pd
# Sample Sprint QA Report Data
sprint_qa_report_data = {
    "Test Case ID": ["TC001", "TC002", "TC003", "TC004", "TC005"],
    "Description": [
        "Log in to Scotiabank",
        "Review available funds",
        "Purchase XRP cryptocurrency",
        "Purchase NVIDIA stock",
        "Log out"
    ],
    "Status": ["Pass", "Pass", "Fail", "Pass", "Pass"],
    "Browser": ["Chrome", "Chrome", "Chrome", "Chrome", "Chrome"],
    "Comments": [
        "Login successful.",
        "Funds displayed correctly.",
        "Unable to confirm XRP purchase.",
        "Stock purchase successful.",
        "Logout successful."
    ]
}

# Create DataFrame
sprint_qa_report = pd.DataFrame(sprint_qa_report_data)
# Save to Excel
output_file_path = "./Sprint_QA_Report.xlsx"
sprint_qa_report.to_excel(output_file_path, index=False, sheet_name="Sprint QA Report")
