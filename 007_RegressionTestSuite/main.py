from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Test Case 1: Log in to the account
def test_login():
    try:
        driver.get("https://cibc.com")
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("P@ssw0rd123")
        driver.find_element(By.ID, "login-button").click()
        assert "Dashboard" in driver.title
        return "Pass", ""
    except Exception as e:
        return "Fail", str(e)

# Execute tests and collect results
results = []
for browser in ["Chrome", "Firefox", "Edge"]:
    # Update driver initialization for each browser here
    status, comment = test_login()
    results.append({
        "Test Case ID": "TC001",
        "Browser": browser,
        "Execution Date": time.strftime("%Y-%m-%d"),
        "Tester": "QA Tester",
        "Status": status,
        "Comments": comment
    })

# Save results to Excel
results_df = pd.DataFrame(results)
results_df.to_excel("./Regression_Test_Results.xlsx", index=False)

