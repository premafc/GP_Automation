import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Loginlocators
from Testdata import logintestdata

class Login:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Loginlocators.username))
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        # Login page password field:
        password_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Loginlocators.password))
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        # Login button:
        login_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Loginlocators.login_button))
        )
        login_button.click()

    def click_ok_button(self):
        # ok button:
        ok_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Loginlocators.ok_button))
        )
        ok_button.click()

    def verify_alert_message(self):
        # Wait for the Alert message and capture its text
        alert_msg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Loginlocators.alert_message))
        )
        invalid_message = alert_msg.text
        return invalid_message

    def verify_locked_alert_message(self):
        # Wait for the Alert message and capture its text
        locked_alert_msg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Loginlocators.account_locked_alert_message))
        )
        locked_alert = locked_alert_msg.text
        return locked_alert

    def verify_login(self):
        # Wait for the welcome message and capture its text
        login_success = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'WELCOME TO GOLDEN PLANET')]"))
        )
        welcome_message = login_success.text
        print("Login Successful. Message:", welcome_message)
        return welcome_message

    def click_my_profile_icon(self):
        time.sleep(2)
        # My profile Icon
        my_profile_icon = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Loginlocators.my_profile_icon))
        )
        my_profile_icon.click()

    def click_logout(self):
        # logout
        time.sleep(2)
        logout = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Loginlocators.logout_text))
        )
        logout.click()
