import pandas as pd

# Bug Report Template Data
bug_report_data = {
    "Bug ID": ["BUG-001"],
    "Title": ["XRP Purchase Fails Despite Sufficient Balance"],
    "Description": [
        "The transaction fails with an error: 'Insufficient Funds' even when the balance shows $500."
    ],
    "Steps to Reproduce": [
        "1. Log in to Scotiabank ITrade.\n"
        "2. Navigate to Coinbase wallet.\n"
        "3. Attempt to purchase $200 in XRP."
    ],
    "Severity": ["High"],
    "Priority": ["Critical"],
    "Reporter": ["QA Analyst"],
    "Status": ["Open"],
    "Assigned To": ["Developer Name"],
    "Environment": ["Chrome, Windows 10"],
    "Comments": ["Possibly a backend validation issue."]
}

bug_report_template = pd.DataFrame(bug_report_data)

# Bug Tracking Sheet Data
bug_tracking_data = {
    "Bug ID": ["BUG-001"],
    "Title": ["XRP Purchase Fails Despite Sufficient Balance"],
    "Status": ["Open"],
    "Assigned To": ["Developer Name"],
    "Priority": ["Critical"],
    "Severity": ["High"],
    "Comments": ["Pending fix confirmation."]
}

bug_tracking_sheet = pd.DataFrame(bug_tracking_data)

# Save Excel file
file_path = "/mnt/data/Bug_Tracking_Workflow.xlsx"
with pd.ExcelWriter(file_path) as writer:
    bug_report_template.to_excel(writer, index=False, sheet_name="Bug Report Template")
    bug_tracking_sheet.to_excel(writer, index=False, sheet_name="Bug Tracking Sheet")

file_path


