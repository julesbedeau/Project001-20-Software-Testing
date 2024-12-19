import pandas as pd

# Creating Test Data
test_data = {
    "Name": ["John Doe", "Jane Smith", "Invalid User", "Weak Password", "Mismatch User"],
    "Email": [
        "john.doe@example.com",
        "jane.smith@example.com",
        "invalid-email",
        "weak.pass@example.com",
        "mismatch@example.com"
    ],
    "Password": ["Pass1234", "Pass5678", "Pass0000", "pass", "Pass1111"],
    "Confirm Password": ["Pass1234", "Pass5678", "Pass0000", "pass", "Pass2222"],
    "Expected Result": [
        "Registration successful",
        "Registration successful",
        "Invalid email format",
        "Password too weak",
        "Passwords do not match"
    ]
}

test_data_df = pd.DataFrame(test_data)

# Save Excel file
file_path = "./Data_Driven_Test_Cases.xlsx"

with pd.ExcelWriter(file_path) as writer:
    test_data_df.to_excel(writer, index=False, sheet_name="Test Data")
