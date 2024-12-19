import pandas as pd

# Creating Test Case Template
test_case_data = {
    "Test Case ID": ["TC001", "TC002", "TC003", "TC004", "TC005"],
    "Module": ["Event Tracking", "Notifications", "Budget Control", "UI", "Payment"],
    "Description": [
        "Add a Birthday Event",
        "Verify Event Reminder Notification",
        "Set Budget for Gift Purchase",
        "Verify Add Event Screen UI Alignment",
        "Purchase a Gift Using Saved Payment Method"
    ],
    "Steps": [
        "1. Launch the app.\n2. Navigate to 'Add Event'.\n3. Enter event details.\n4. Save.",
        "1. Add an event with a reminder.\n2. Wait for the scheduled reminder.",
        "1. Navigate to settings.\n2. Set budget for gifts.\n3. Save settings.",
        "1. Launch the app.\n2. Navigate to 'Add Event'.",
        "1. Navigate to the 'Gifts' section.\n2. Select a gift.\n3. Complete purchase."
    ],
    "Expected Result": [
        "Event is added and visible in the timeline.",
        "Notification is received at the correct time.",
        "Budget is saved and applied during gift purchase.",
        "All UI elements are properly aligned, visible, and functional.",
        "Purchase is successful, and a confirmation is displayed."
    ]
}

test_case_template = pd.DataFrame(test_case_data)

# Creating Defect Report Template
defect_report_data = {
    "Defect ID": ["DEF001", "DEF002"],
    "Test Case ID": ["TC004", "TC005"],
    "Module": ["UI", "Payment"],
    "Description": [
        "Misaligned buttons on the Add Event screen",
        "Payment method not saved"
    ],
    "Severity": ["Medium", "High"],
    "Steps to Reproduce": [
        "1. Launch the app.\n2. Navigate to 'Add Event'.",
        "1. Navigate to 'Gifts'.\n2. Select a gift.\n3. Use saved payment method."
    ],
    "Expected Result": [
        "Buttons should be properly aligned and functional.",
        "Payment completes successfully."
    ],
    "Actual Result": [
        "Buttons appear misaligned on small-screen devices.",
        "Payment fails with 'Payment method not available' error."
    ],
    "Status": ["Open", "Open"]
}

defect_report_template = pd.DataFrame(defect_report_data)

# Save Excel file
file_path = "./Mobile_App_Testing.xlsx"

with pd.ExcelWriter(file_path) as writer:
    test_case_template.to_excel(writer, index=False, sheet_name="Test Cases")
    defect_report_template.to_excel(writer, index=False, sheet_name="Defect Report")


