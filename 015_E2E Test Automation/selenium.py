from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Log in
    driver.get("https://www.scotiabank.com/itrade")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("your_username")
    driver.find_element(By.ID, "password").send_keys("your_password")
    driver.find_element(By.ID, "login-button").click()

    # Step 2: Review funds available
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "funds-tab"))).click()
    funds = driver.find_element(By.ID, "available-funds").text
    print(f"Available funds: {funds}")

    # Step 3: Purchase $200 in XRP cryptocurrency
    driver.get("https://www.coinbase.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys("your_coinbase_email")
    driver.find_element(By.ID, "password").send_keys("your_coinbase_password")
    driver.find_element(By.ID, "signin-button").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "buy-sell-tab"))).click()
    driver.find_element(By.ID, "crypto-type").send_keys("XRP")
    driver.find_element(By.ID, "amount").send_keys("200")
    driver.find_element(By.ID, "confirm-button").click()

    # Step 4: Purchase three shares of NVIDIA
    driver.get("https://www.scotiabank.com/itrade/trade")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "symbol"))).send_keys("NVDA")
    driver.find_element(By.ID, "quantity").send_keys("3")
    driver.find_element(By.ID, "trade-button").click()

    # Step 5: Log out
    driver.find_element(By.ID, "logout-button").click()
    print("Test completed successfully.")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    driver.quit()
