from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        # Step 1: Log in
        page.goto("https://www.scotiabank.com/itrade")
        page.fill("#username", "your_username")
        page.fill("#password", "your_password")
        page.click("#login-button")

        # Step 2: Review funds available
        page.wait_for_selector("#funds-tab")
        page.click("#funds-tab")
        funds = page.text_content("#available-funds")
        print(f"Available funds: {funds}")

        # Step 3: Purchase $200 in XRP cryptocurrency
        page.goto("https://www.coinbase.com/login")
        page.fill("#email", "your_coinbase_email")
        page.fill("#password", "your_coinbase_password")
        page.click("#signin-button")
        page.click("#buy-sell-tab")
        page.fill("#crypto-type", "XRP")
        page.fill("#amount", "200")
        page.click("#confirm-button")

        # Step 4: Purchase three shares of NVIDIA
        page.goto("https://www.scotiabank.com/itrade/trade")
        page.fill("#symbol", "NVDA")
        page.fill("#quantity", "3")
        page.click("#trade-button")

        # Step 5: Log out
        page.click("#logout-button")
        print("Test completed successfully.")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        browser.close()
