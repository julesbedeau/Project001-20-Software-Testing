# Creating Exploratory Testing Plan Data
exploratory_testing_plan_data = {
    "Session ID": ["S001", "S002", "S003", "S004"],
    "Objective": [
        "Explore login functionality with valid/invalid credentials",
        "Explore funds review page for accuracy and data loading",
        "Explore cryptocurrency purchase flow for XRP on Coinbase",
        "Explore stock purchase workflow for NVIDIA stock"
    ],
    "Charter": [
        "Validate system behavior with various input scenarios.",
        "Verify funds data accuracy, error messages, and page loading speed.",
        "Identify defects or inconsistencies in XRP purchase flow.",
        "Test NVDA stock trading execution with different inputs."
    ],
    "Test Techniques": [
        "Equivalence Partitioning, Boundary Value Analysis",
        "Error Guessing, Data Validation",
        "Workflow Validation, Negative Testing",
        "Scenario-based Testing, Input Validation"
    ],
    "Duration": ["60 min", "60 min", "90 min", "90 min"],
    "Test Notes": [
        "Observe login success, failure, and error handling.",
        "Validate accuracy of available funds and edge cases.",
        "Check purchase confirmation, failures, and messages.",
        "Confirm stock purchase completion and data integrity."
    ],
    "Bugs Identified": [2, 1, 3, 1]
}

# Creating Session-Based Test Report Data
session_based_report_data = {
    "Session ID": ["S001", "S002", "S003", "S004"],
    "Tester": ["QA1", "QA1", "QA2", "QA2"],
    "Bugs Logged": [2, 1, 3, 1],
    "Key Observations": [
        "Error messages not displayed for invalid credentials.",
        "Funds page slow to load with large data sets.",
        "XRP purchase failed with insufficient balance.",
        "NVDA stock purchase successful with minor UI glitches."
    ],
    "Follow-up Actions": [
        "Fix error message handling for invalid inputs.",
        "Optimize funds page for better performance.",
        "Resolve issues with XRP purchase flow.",
        "Fix minor UI issues on trade confirmation."
    ],
    "Status": ["Completed", "Completed", "Completed", "In Progress"]
}

# Creating DataFrames
exploratory_testing_plan = pd.DataFrame(exploratory_testing_plan_data)
session_based_report = pd.DataFrame(session_based_report_data)

# Save to Excel
output_file_path = "./Exploratory_Testing_Plan_and_Report.xlsx"
with pd.ExcelWriter(output_file_path) as writer:
    exploratory_testing_plan.to_excel(writer, index=False, sheet_name="Exploratory Testing Plan")
    session_based_report.to_excel(writer, index=False, sheet_name="Session Based Report")

output_file_path

# Re-import necessary library after code execution environment reset
import pandas as pd

# Creating Exploratory Testing Plan Data
exploratory_testing_plan_data = {
    "Session ID": ["S001", "S002", "S003", "S004"],
    "Objective": [
        "Explore login functionality with valid/invalid credentials",
        "Explore funds review page for accuracy and data loading",
        "Explore cryptocurrency purchase flow for XRP on Coinbase",
        "Explore stock purchase workflow for NVIDIA stock"
    ],
    "Charter": [
        "Validate system behavior with various input scenarios.",
        "Verify funds data accuracy, error messages, and page loading speed.",
        "Identify defects or inconsistencies in XRP purchase flow.",
        "Test NVDA stock trading execution with different inputs."
    ],
    "Test Techniques": [
        "Equivalence Partitioning, Boundary Value Analysis",
        "Error Guessing, Data Validation",
        "Workflow Validation, Negative Testing",
        "Scenario-based Testing, Input Validation"
    ],
    "Duration": ["60 min", "60 min", "90 min", "90 min"],
    "Test Notes": [
        "Observe login success, failure, and error handling.",
        "Validate accuracy of available funds and edge cases.",
        "Check purchase confirmation, failures, and messages.",
        "Confirm stock purchase completion and data integrity."
    ],
    "Bugs Identified": [2, 1, 3, 1]
}

# Creating Session-Based Test Report Data
session_based_report_data = {
    "Session ID": ["S001", "S002", "S003", "S004"],
    "Tester": ["QA1", "QA1", "QA2", "QA2"],
    "Bugs Logged": [2, 1, 3, 1],
    "Key Observations": [
        "Error messages not displayed for invalid credentials.",
        "Funds page slow to load with large data sets.",
        "XRP purchase failed with insufficient balance.",
        "NVDA stock purchase successful with minor UI glitches."
    ],
    "Follow-up Actions": [
        "Fix error message handling for invalid inputs.",
        "Optimize funds page for better performance.",
        "Resolve issues with XRP purchase flow.",
        "Fix minor UI issues on trade confirmation."
    ],
    "Status": ["Completed", "Completed", "Completed", "In Progress"]
}

# Creating DataFrames
exploratory_testing_plan = pd.DataFrame(exploratory_testing_plan_data)
session_based_report = pd.DataFrame(session_based_report_data)

# Save to Excel
output_file_path = "./Exploratory_Testing_Plan_and_Report.xlsx"
with pd.ExcelWriter(output_file_path) as writer:
    exploratory_testing_plan.to_excel(writer, index=False, sheet_name="Exploratory Testing Plan")
    session_based_report.to_excel(writer, index=False, sheet_name="Session Based Report")

