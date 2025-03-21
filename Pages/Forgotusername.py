import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils import db_utils
from Locators import Forogotusernamelocators
from Testdata import Forgotusernametestdata

class Forgotusername:
 
    def __init__(self, driver):
        self.driver = driver

    def forgot_user_name(self, driver):
        try:
            # Forgot username link :
            forgot_username_link = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forogotusernamelocators.Forgot_User_Name))
            )
            forgot_username_link.click()

            # Date of birth field:
            date_of_birth_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Forogotusernamelocators.Date_of_birth))
            )
            date_of_birth_field.click()
            time.sleep(3)
            # Date of birth field backward:
            date_of_birth_field_backward = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Forogotusernamelocators.Date_previous_button))
            )
            date_of_birth_field_backward.click()
            """
            time.sleep(2)
            date_of_birth_field_backward.click()
            time.sleep(2)
            date_of_birth_field_backward.click()
            time.sleep(2)
            date_of_birth_field_backward.click()
            time.sleep(2)
            date_of_birth_field_backward.click()
            time.sleep(2)
            date_of_birth_field_backward.click()

            time.sleep(2)
            """
            # Date of birth field date:
            date_of_birth_field_date = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, Forogotusernamelocators.Date_month))
            )
            date_of_birth_field_date.click()

            # Mobile number field drop down clicked
            dropdown = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forogotusernamelocators.Mobile_Number_dropdown)))
            dropdown.click()
            time.sleep(2)

            # Mobile number field drop down India clicked
            dp_india = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forogotusernamelocators.India)))
            dp_india.click()
            time.sleep(2)

            # Filled the Mobile number:
            mobile_number_field = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forogotusernamelocators.Mobile_Number_Input_field)))
            mobile_number_field.send_keys(Forgotusernametestdata.mobile_number)

            # Send OTP button:
            Request_OTP = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forogotusernamelocators.Mobile_number_Request_OTP))
            )
            Request_OTP.click()

            # Pause to allow OTP to be sent and stored in the database
            time.sleep(5)  # Adjust sleep time as needed

            # Fetch the latest mobile OTP from the database
            # mobile_otp = db_utils.fetch_latest_mobile_otp_by_number(locator.mobile_number)
            mobile_otp = db_utils.fetch_latest_mobile_otp_by_number(Forgotusernametestdata.mobile_number)
            if not mobile_otp:
                print("Failed to retrieve mobile OTP")
                return

            # Enter the OTP in the respective OTP field
            mobile_number_otp_field = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, Forogotusernamelocators.Mobile_Number_OTP_field)))
            mobile_number_otp_field.send_keys(mobile_otp)

            # Click on the Verify button.
            verify_button_mn = driver.find_element(By.XPATH, Forogotusernamelocators.Mobile_Number_Verify_button)
            verify_button_mn.click()
            print("Mobile number OTP verified.")

            success_popup = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, Forogotusernamelocators.Success_POP_UP))
            )
            # Click the OK button
            success_popup.click()
            print("Success: Forgot UserName Successfully. ")

        except Exception as Forgot_username_Error:
            print("Forgot username functionality Error.", Forgot_username_Error)


