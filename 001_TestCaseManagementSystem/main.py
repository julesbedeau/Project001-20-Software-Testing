import pandas as pd

# Creating Test Case Template
test_case_data = {
    "Test Case ID": ["TC001", "TC002", "TC003", "TC004"],
    "Description": [
        "Log in to CIBC chequing account",
        "Review account balance",
        "Pay Hydro One bill ($300)",
        "Sign out"
    ],
    "Preconditions": [
        "User has valid credentials. Browser open on login page.",
        "User is logged in.",
        "User is logged in. Bill Payee added.",
        "User is logged in."
    ],
    "Steps": [
        "1. Open the browser.\n2. Navigate to cibc.com.\n3. Enter username and password.\n4. Click 'Sign In'.",
        "1. Click 'Accounts'.\n2. Select the chequing account.",
        "1. Click 'Payments'.\n2. Select 'Hydro One' as payee.\n3. Enter $300.\n4. Confirm payment.",
        "1. Click 'Sign Out'."
    ],
    "Expected Result": [
        "User successfully logs into the account.",
        "Balance is displayed correctly.",
        "Payment is processed successfully.",
        "User is logged out."
    ],
    "Actual Result": ["", "", "", ""],
    "Status": ["", "", "", ""],
    "Comments": ["", "", "", ""]
}

test_case_template = pd.DataFrame(test_case_data)

# Creating Test Plan Template
test_plan_data = {
    "Task": ["Test Case Design", "Test Execution", "Reporting & Review"],
    "Start Date": ["Nov 19, 2024", "Nov 21, 2024", "Nov 24, 2024"],
    "End Date": ["Nov 20, 2024", "Nov 23, 2024", "Nov 24, 2024"],
    "Responsible": ["QA Analyst", "QA Analyst", "QA Lead"]
}

test_plan_template = pd.DataFrame(test_plan_data)

# Creating Execution Report Template
execution_report_data = {
    "Test Case ID": ["TC001", "TC001", "TC001", "TC001", "TC002", "TC003", "TC004"],
    "Browser": ["Safari", "Chrome", "Firefox", "Edge", "Safari", "Chrome", "Edge"],
    "Execution Date": [
        "Nov 21, 2024", "Nov 21, 2024", "Nov 21, 2024", "Nov 21, 2024",
        "Nov 21, 2024", "Nov 21, 2024", "Nov 21, 2024"
    ],
    "Tester": ["Jane Doe", "Jane Doe", "Jane Doe", "Jane Doe", "Jane Doe", "Jane Doe", "Jane Doe"],
    "Status": ["Pass", "Pass", "Fail", "Pass", "Pass", "Pass", "Pass"],
    "Comments": [
        "Successfully logged in.", "Successfully logged in.", 
        "Login button not responsive.", "Successfully logged in.",
        "Account balance displayed correctly.", 
        "Payment processed without errors.",
        "User logged out successfully."
    ]
}

execution_report_template = pd.DataFrame(execution_report_data)

# Save all templates to an Excel file
with pd.ExcelWriter("./Test_Case_Management_System.xlsx") as writer:
    test_case_template.to_excel(writer, index=False, sheet_name="Test Case Template")
    test_plan_template.to_excel(writer, index=False, sheet_name="Test Plan Template")
    execution_report_template.to_excel(writer, index=False, sheet_name="Execution Report")
