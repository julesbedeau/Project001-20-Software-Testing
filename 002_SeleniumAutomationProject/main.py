import pandas as pd

# Creating Test Case Template
test_case_template_data = {
    "Test Case ID": ["TC001", "TC002", "TC003", "TC004", "TC005"],
    "Description": [
        "Log in to Scotiabank ITrade",
        "Review available funds",
        "Purchase XRP cryptocurrency",
        "Purchase NVIDIA stock",
        "Log out"
    ],
    "Preconditions": [
        "Valid credentials",
        "User is logged in",
        "Valid Coinbase login",
        "User is logged in",
        "User is logged in"
    ],
    "Steps": [
        "Enter credentials and click login.",
        "Navigate to the funds tab.",
        "Complete purchase flow on Coinbase.",
        "Execute trade for NVDA stock.",
        "Click the logout button."
    ],
    "Expected Result": [
        "User is successfully logged in.",
        "Funds are displayed correctly.",
        "XRP purchase is completed.",
        "Stock purchase is confirmed.",
        "User is successfully logged out."
    ]
}

test_case_template = pd.DataFrame(test_case_template_data)

# Creating Test Report Template
test_report_data = {
    "Test Case ID": ["TC001", "TC002", "TC003", "TC004", "TC005"],
    "Browser": ["Chrome", "Chrome", "Chrome", "Chrome", "Chrome"],
    "Status": ["Pass", "Pass", "Fail", "Pass", "Pass"],
    "Comments": [
        "Login successful.",
        "Funds displayed correctly.",
        "Unable to confirm XRP purchase.",
        "Stock purchase successful.",
        "Logout successful."
    ]
}

test_report_template = pd.DataFrame(test_report_data)

# Save all templates and reports to an Excel file
file_path = "./Selenium_Automation_Project01.xlsx"

with pd.ExcelWriter(file_path) as writer:
    test_case_template.to_excel(writer, index=False, sheet_name="Test Case Template")
    test_report_template.to_excel(writer, index=False, sheet_name="Test Report")



# Recreating Test Case Template
test_case_template_data = {
    "Test Case ID": ["TC001", "TC002", "TC003", "TC004", "TC005"],
    "Description": [
        "Log in to Scotiabank ITrade",
        "Review available funds",
        "Purchase XRP cryptocurrency",
        "Purchase NVIDIA stock",
        "Log out"
    ],
    "Preconditions": [
        "Valid credentials",
        "User is logged in",
        "Valid Coinbase login",
        "User is logged in",
        "User is logged in"
    ],
    "Steps": [
        "Enter credentials and click login.",
        "Navigate to the funds tab.",
        "Complete purchase flow on Coinbase.",
        "Execute trade for NVDA stock.",
        "Click the logout button."
    ],
    "Expected Result": [
        "User is successfully logged in.",
        "Funds are displayed correctly.",
        "XRP purchase is completed.",
        "Stock purchase is confirmed.",
        "User is successfully logged out."
    ]
}

test_case_template = pd.DataFrame(test_case_template_data)

# Recreating Test Report Template
test_report_data = {
    "Test Case ID": ["TC001", "TC002", "TC003", "TC004", "TC005"],
    "Browser": ["Chrome", "Chrome", "Chrome", "Chrome", "Chrome"],
    "Status": ["Pass", "Pass", "Fail", "Pass", "Pass"],
    "Comments": [
        "Login successful.",
        "Funds displayed correctly.",
        "Unable to confirm XRP purchase.",
        "Stock purchase successful.",
        "Logout successful."
    ]
}

test_report_template = pd.DataFrame(test_report_data)

# Save all templates and reports to an Excel file
file_path = "./Selenium_Automation_Project02.xlsx"

with pd.ExcelWriter(file_path) as writer:
    test_case_template.to_excel(writer, index=False, sheet_name="Test Case Template")
    test_report_template.to_excel(writer, index=False, sheet_name="Test Report")



