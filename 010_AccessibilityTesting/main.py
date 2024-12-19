# Creating Accessibility Test Case Template
accessibility_test_cases = {
    "Test Case ID": ["TC001", "TC002", "TC003", "TC004", "TC005"],
    "Description": [
        "Ensure color contrast is distinguishable",
        "Provide captions for audio messages",
        "Verify screen reader compatibility",
        "Test multilingual support",
        "Validate form field accessibility"
    ],
    "Steps": [
        "1. Launch the app.\n2. Inspect UI components (buttons, text).",
        "1. Send a video or audio message.\n2. Verify captions are generated or provided manually.",
        "1. Enable screen reader (VoiceOver, TalkBack).\n2. Navigate through app features.",
        "1. Switch language to Spanish or French.\n2. Verify translations in UI and content.",
        "1. Navigate to 'Add Event'.\n2. Check form field labels."
    ],
    "Expected Result": [
        "All text meets minimum contrast ratio of 4.5:1.",
        "Captions are available for all audio/video messages.",
        "Screen reader announces all interactive elements and content.",
        "UI text and notifications appear correctly in the selected language.",
        "Labels are visible and announced by the screen reader."
    ]
}

test_case_template = pd.DataFrame(accessibility_test_cases)

# Creating Accessibility Defect Report Template
accessibility_defects = {
    "Defect ID": ["DEF001", "DEF002", "DEF003"],
    "Test Case ID": ["TC001", "TC002", "TC003"],
    "Description": [
        "Low color contrast on 'Add Event' button",
        "No captions for video messages",
        "Screen reader skips navigation bar"
    ],
    "Severity": ["High", "Critical", "Medium"],
    "Steps to Reproduce": [
        "1. Launch the app.\n2. Navigate to 'Dashboard'.",
        "1. Send a video message.\n2. Check for captions.",
        "1. Enable screen reader.\n2. Navigate to 'Settings'."
    ],
    "Expected Result": [
        "Button color contrast meets 4.5:1 ratio.",
        "Captions are displayed for the video.",
        "Navigation bar elements are announced by the screen reader."
    ],
    "Actual Result": [
        "Button color contrast is 3:1, making it hard to distinguish.",
        "Captions are missing.",
        "Screen reader skips navigation bar entirely."
    ],
    "Status": ["Open", "Open", "Open"]
}

defect_report_template = pd.DataFrame(accessibility_defects)

# Save Excel file
file_path = "/mnt/data/Accessibility_Testing_Results.xlsx"

with pd.ExcelWriter(file_path) as writer:
    test_case_template.to_excel(writer, index=False, sheet_name="Test Cases")
    defect_report_template.to_excel(writer, index=False, sheet_name="Defect Report")

file_path

