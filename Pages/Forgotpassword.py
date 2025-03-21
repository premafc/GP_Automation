"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils import db_utils
from Locators import Forgotpasswordlocators
from Testdata import Forgotpasswordtestdata

class ForgotPassword:

    def __init__(self, driver):
        self.driver = driver

    def forgot_password(self, driver):
        try:
            # Forgot password link :
            forgot_password_link = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Forgot_password))
            )
            forgot_password_link.click()

            # Enter the user Email id:
            email_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Forgot_password_Email))
            )
            email_field.send_keys(Forgotpasswordtestdata.email)

            # Request OTP button:
            Request_otp_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Email_Request_OTP))
            )
            Request_otp_button.click()

            # Pause to allow OTP to be sent and stored in the database
            time.sleep(5)  # Adjust sleep time as needed

            # Fetch the latest email OTP from the database
            #email_otp = db_utils.fetch_latest_email_otp_by_email(Forgotpasswordlocators.Forgot_password_Email)
            email_otp = db_utils.fetch_latest_email_otp_by_email(Forgotpasswordtestdata.email)
            print(email_otp)
            if not email_otp:
                print("Failed to retrieve email OTP")
                return

            # Enter the Email otp field.
            otp_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Email_OTP_Field)))
            otp_field.send_keys(email_otp)

            # Click on the Verify button.
            verify_button = driver.find_element(By.XPATH, Forgotpasswordlocators.Verify_button)
            verify_button.click()
            print("Email OTP Verified")
            time.sleep(2)

            # Mobile number field drop down clicked
            dropdown = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Mobile_Number_dropdown)))
            dropdown.click()
            time.sleep(2)

            # Mobile number field drop down India clicked
            dp_india = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.India)))
            dp_india.click()
            time.sleep(2)

            # Filled the Mobile number:
            mobile_number_field = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Mobile_Number_Input_field)))
            mobile_number_field.send_keys(Forgotpasswordtestdata.mobile_number)

            # Request OTP button:
            Request_otp_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Mobile_number_Request_OTP))
            )
            Request_otp_button.click()

            # Pause to allow OTP to be sent and stored in the database
            time.sleep(5)  # Adjust sleep time as needed

            # Fetch the latest mobile OTP from the database
            #mobile_otp = db_utils.fetch_latest_mobile_otp_by_number(Forgotpasswordlocators.Mobile_Number_OTP_field)
            mobile_otp = db_utils.fetch_latest_mobile_otp_by_number(Forgotpasswordtestdata.mobile_number)
            if not mobile_otp:
                print("Failed to retrieve mobile OTP")
                return

            # Enter the OTP in the respective OTP field
            mobile_number_otp_field = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Mobile_Number_OTP_field)))
            mobile_number_otp_field.send_keys(mobile_otp)

            # Click on the Verify button.
            verify_button_mn = driver.find_element(By.XPATH, Forgotpasswordlocators.Mobile_Number_Verify_button)
            verify_button_mn.click()
            print("Mobile number OTP verified.")

            success = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[text() = 'Password Has Been Sent To Your Email Address']"))
            )
            log = success.text
            print(log)

            success_popup = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Forgotpasswordlocators.Success_POP_UP))
            )
            # Click the OK button
            success_popup.click()
            return log
            # "//*[text() = 'OTP Verified Successfully']"
        except Exception as Forgot_Password_Error:
            print("Forgot password Error. ", Forgot_Password_Error)

"""

import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Forgotpasswordlocators
from Testdata import Forgotpasswordtestdata
from Utils import db_utils

class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver

    def click_forgot_password_link(self):
        fp_link = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Forgot_password))
        )
        fp_link.click()

    def enter_email(self, email):
        email_id_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Forgot_password_Email))
        )
        time.sleep(2)
        email_id_field.send_keys(email)

    def clear_email(self):
        email_id_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Forgot_password_Email))
        )
        email_id_field.send_keys(Keys.CONTROL + "a")
        email_id_field.send_keys(Keys.DELETE)

    def click_request_otp_button_email(self):
        request_otp_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Email_Request_OTP))
        )
        request_otp_button.click()
        time.sleep(5)

    def click_resend_otp_link_email(self):
        resend_otp_link = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Resend_OTP_Link_Email))
        )
        resend_otp_link.click()
        time.sleep(5)

    def fetch_email_otp_and_enter_email_otp(self):
        email_otp = db_utils.fetch_latest_email_otp_by_email(Forgotpasswordtestdata.email)
        print(email_otp)
        if not email_otp:
            print("Failed to retrieve email OTP")
            return
        email_otp_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Email_OTP_Field))
        )
        email_otp_field.send_keys(email_otp)

    def enter_email_otp(self, email_otp):
        email_otp_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Email_OTP_Field))
        )
        email_otp_field.send_keys(email_otp)

    def clear_email_otp(self):
        email_otp_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Email_OTP_Field))
        )
        email_otp_field.send_keys(Keys.CONTROL + "a")
        email_otp_field.send_keys(Keys.DELETE)

    def click_email_otp_verify_button(self):
        verify_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Verify_button))
        )
        verify_button.click()
        time.sleep(2)

    def select_dropdown_option(self):
        dropdown = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Mobile_Number_dropdown))
        )
        dropdown.click()
        time.sleep(2)

    def select_india_dropdown_option(self):
        dropdown = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.India))
        )
        dropdown.click()

    def enter_mobile_number(self, mobile_number):
        mobile_number_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Mobile_Number_Input_field))
        )
        mobile_number_field.send_keys(mobile_number)

    def clear_mobile_number(self):
        mobile_number_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Mobile_Number_Input_field))
        )
        for _ in range(len(mobile_number_field.get_attribute("value"))):
            mobile_number_field.send_keys(Keys.BACKSPACE)
        time.sleep(5)
        #mobile_number_field.send_keys(Keys.CONTROL + "a")
        #mobile_number_field.send_keys(Keys.DELETE)

    def click_request_otp_button_mobile_number(self):
        request_otp_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Mobile_number_Request_OTP))
        )
        request_otp_button.click()
        time.sleep(5)

    def fetch_mobile_otp_and_enter_mobile_otp(self):
        mobile_otp = db_utils.fetch_latest_mobile_otp_by_number(Forgotpasswordtestdata.mobile_number)
        print(mobile_otp)
        if not mobile_otp:
            print("Failed to retrieve email OTP")
            return
        mobile_otp_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Mobile_Number_OTP_field))
        )
        mobile_otp_field.send_keys(mobile_otp)

    def click_mobile_otp_verify_button(self):
        verify_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Mobile_Number_Verify_button))
        )
        verify_button.click()
        time.sleep(2)

    def enter_mobile_otp(self, mobile_otp):
        mobile_otp_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Mobile_Number_OTP_field))
        )
        mobile_otp_field.send_keys(mobile_otp)

    def clear_mobile_otp(self):
        email_otp_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Forgotpasswordlocators.Mobile_Number_OTP_field))
        )
        email_otp_field.send_keys(Keys.CONTROL + "a")
        email_otp_field.send_keys(Keys.DELETE)

    def click_resend_otp_link_mobile_number(self):
        resend_otp_link = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Resend_OTP_Link_Mobile))
        )
        resend_otp_link.click()
        time.sleep(5)

    def verify_and_get_success_message(self):
        # Wait for the welcome message and capture its text
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[text() = 'OTP Verified Successfully']"))
        )
        #welcome_message = success_message.text
        print("Forgot password pop up message : ", success_message)
        return success_message.text.split('\n')[0]

    def click_popup_ok_button(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Forgotpasswordlocators.Success_POP_UP))
        ).click()
        print("Forgot Password pop up message : OTP Verified Successfully Password Has Been Sent To Your Email Address")
