import pandas as pd

# Creating Execution Results Data
execution_results = {
    "Step": [
        "Log in",
        "Review funds available",
        "Purchase XRP cryptocurrency",
        "Purchase NVIDIA stock",
        "Log out"
    ],
    "Expected Result": [
        "User logs in successfully.",
        "Funds displayed correctly.",
        "XRP purchase confirmation message displayed.",
        "Stock purchase confirmation message displayed.",
        "User logs out successfully."
    ],
    "Actual Result": [
        "Success",
        "Success",
        "Failed",
        "Success",
        "Success"
    ],
    "Status": ["Pass", "Pass", "Fail", "Pass", "Pass"],
    "Comments": [
        "",
        "",
        "Insufficient funds error.",
        "",
        ""
    ]
}

execution_results_df = pd.DataFrame(execution_results)

# Save to Excel file
file_path = "./E2E_Test_Automation_Results.xlsx"

with pd.ExcelWriter(file_path) as writer:
    execution_results_df.to_excel(writer, index=False, sheet_name="Execution Results")
