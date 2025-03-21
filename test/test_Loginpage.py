import pytest
import allure
from allure_commons.types import AttachmentType
from Pages.Loginpage import Login  # If 'Pages' is inside another directory
from Testdata import logintestdata
import time
import HtmlTestRunner
import unittest


@pytest.mark.usefixtures("setup_class")
class TestLogin:
    driver = None  # Explicitly define the driver attribute
    #url = "https://gold.groupnpay.com/#/"

    def __init__(self, driver=None):  # Accept driver in the constructor
        self.driver = driver

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_invalid_login(self):
        try:
            login_page = Login(self.driver)
            # Case 1 : Login with Invalid username and invalid password.
            login_page.enter_username(logintestdata.Invalid_Username)
            login_page.enter_password(logintestdata.Invalid_Password)
            login_page.click_login_button()
            msg = login_page.verify_alert_message()
            login_page.click_ok_button()

            # Case 2 : Login with Valid username and Incorrect password:
            login_page.enter_username(logintestdata.valid_username)
            login_page.enter_password(logintestdata.Invalid_Password)
            login_page.click_login_button()
            login_page.click_ok_button()

            # Case 3 : Login with Incorrect username and valid_password:
            login_page.enter_username(logintestdata.Incorrect_username_1)
            login_page.enter_password(logintestdata.valid_password)
            login_page.click_login_button()
            login_page.click_ok_button()

            login_page.enter_username(logintestdata.Incorrect_username_2)
            login_page.click_login_button()
            login_page.enter_username(logintestdata.Incorrect_username_3)
            login_page.click_login_button()
            login_page.enter_username(logintestdata.Incorrect_username_4)
            login_page.click_login_button()
            login_page.enter_username(logintestdata.Incorrect_username_5)
            login_page.click_login_button()
            login_page.enter_username(logintestdata.Incorrect_username_6)
            login_page.click_login_button()
            login_page.enter_username(logintestdata.Incorrect_username_7)
            login_page.click_login_button()

            # Case 4 : Login with Empty Credentials:
            login_page.click_login_button()

            assert msg == 'Invalid credentials', 'f Test Failed : Invalid credentials'
        except Exception as Invalid_Login_Error:
            allure.attach(self.driver.get_screenshot_as_png(), name="Test Invalid Login",
                          attachment_type=AttachmentType.PNG)
            print("Invalid Login Errors.", Invalid_Login_Error)

    @allure.severity(allure.severity_level.NORMAL)
    def test_locked_account(self):
        try:
            login_page = Login(self.driver)
            login_page.enter_username(logintestdata.locked_username)
            login_page.enter_password(logintestdata.locked_password)
            login_page.click_login_button()
            msg = login_page.verify_locked_alert_message()
            login_page.click_ok_button()

            assert msg == 'You have attempted more than 3 times. Please click on forgot password', 'f Test Failed : You have attempted more than 3 times. Please click on forgot password'
        except Exception as Locked_Account_Error:
            print("Locked Account Error.", Locked_Account_Error)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_sql_injection(self):
        try:
            login_page = Login(self.driver)
            login_page.enter_username(logintestdata.SQL_Injection_Username)
            login_page.enter_password(logintestdata.valid_password)
            login_page.click_login_button()

        except Exception as SQL_Injection_Error:
            print("SQL Injection Error Failed. ", SQL_Injection_Error)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_login(self):
        login_page = Login(self.driver)
        # Pass the username and password for login
        login_page.enter_username(logintestdata.valid_username)
        login_page.enter_password(logintestdata.valid_password)
        login_page.click_login_button()
        time.sleep(10)
        """
        # Verify the login and print the welcome message
        welcome_message = obj_login.verify_login()
        assert "WELCOME TO GOLDEN PLANET" in welcome_message, "Login was not successful."
        """

    @allure.severity(allure.severity_level.BLOCKER)
    def test_user_logout(self):
        time.sleep(3)
        login_page = Login(self.driver)
        login_page.click_my_profile_icon()
        login_page.click_logout()

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_approver_login(self):
        login_page = Login(self.driver)
        login_page.enter_username(logintestdata.approver_username)
        login_page.enter_password(logintestdata.approver_password)
        login_page.click_login_button()
        time.sleep(5)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='html_report',
        report_title='Golden planet Automation Test Results',
        descriptions='Test results for Goldenplanet automation scripts'
    ))
