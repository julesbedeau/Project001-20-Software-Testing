from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# BrowserStack Configuration
BROWSERSTACK_USERNAME = "your_browserstack_username"
BROWSERSTACK_ACCESS_KEY = "your_browserstack_access_key"

def get_browserstack_driver(browser, os_name, os_version):
    capabilities = {
        "os": os_name,
        "os_version": os_version,
        "browser": browser,
        "browser_version": "latest",
        "name": f"CrossBrowserTest-{browser}-{os_name}-{os_version}",
        "build": "Cross-Browser Testing Suite"
    }
    driver = webdriver.Remote(
        command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=capabilities,
    )
    return driver

# Define test cases
def test_login(driver):
    try:
        driver.get("https://www.scotiaitrade.com/")
        time.sleep(2)  # Let the page load
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("P@ssw0rd123")
        driver.find_element(By.ID, "sign-in-btn").click()
        time.sleep(2)
        assert "Dashboard" in driver.title
        print("Login Test Passed")
    except Exception as e:
        print(f"Login Test Failed: {e}")
    finally:
        driver.quit()

# List of browsers and configurations
browsers = [
    {"browser": "Chrome", "os_name": "Windows", "os_version": "11"},
    {"browser": "Firefox", "os_name": "Windows", "os_version": "11"},
    {"browser": "Edge", "os_name": "Windows", "os_version": "11"},
    {"browser": "Safari", "os_name": "OS X", "os_version": "Ventura"},
]

# Run tests for all browser configurations
for config in browsers:
    print(f"Testing on {config['browser']} ({config['os_name']} {config['os_version']})")
    driver = get_browserstack_driver(config["browser"], config["os_name"], config["os_version"])
    test_login(driver)

