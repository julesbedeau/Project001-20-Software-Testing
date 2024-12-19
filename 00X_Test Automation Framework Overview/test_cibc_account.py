import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.config_loader import load_config
from utilities.data_loader import load_test_data

class TestCIBCAccount:
    config = load_config('./config/test_credentials.yaml')
    test_data = load_test_data('./config/test_data.yaml')

    @pytest.fixture(scope="class")
    def setup(self):
        driver_path = './drivers/chromedriver'
        self.driver = webdriver.Chrome(driver_path)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_login(self, setup):
        cibc_config = self.config['cibc']
        self.driver.get("https://www.cibc.com")
        self.driver.find_element(By.ID, "username").send_keys(cibc_config['username'])
        self.driver.find_element(By.ID, "password").send_keys(cibc_config['password'])
        self.driver.find_element(By.ID, "login-button").click()
        assert "Dashboard" in self.driver.title

    def test_make_payment(self, setup):
        transaction = self.test_data['transactions'][0]
        self.driver.find_element(By.ID, "payments-tab").click()
        self.driver.find_element(By.ID, "payee").send_keys(transaction['payee'])
        self.driver.find_element(By.ID, "amount").send_keys(transaction['amount'])
        self.driver.find_element(By.ID, "confirm-button").click()
        assert "Payment successful" in self.driver.page_source
