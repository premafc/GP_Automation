import pytest
import time
#from Pages.Forgotpassword import ForgotPassword
from Pages.Forgotpassword import ForgotPasswordPage
from Testdata import Forgotpasswordtestdata

@pytest.mark.usefixtures("setup_class")
class Testforgotpassword:

    driver = None  # Explicitly define the driver attribute

    """
    def test_01_forgot_password(self):
        time.sleep(2)
        obj_Forgotpassword = ForgotPassword(self.driver)
        obj_Forgotpassword.forgot_password(self.driver)
    """
    @pytest.mark.id("TC-FP-002")
    def test_01_forgot_password_email_validation(self):
        try:
            forgot_password = ForgotPasswordPage(self.driver)
            forgot_password.click_forgot_password_link()
            # Invalid E-mail Address:
            forgot_password.enter_email(Forgotpasswordtestdata.incorrect_email_1)
            forgot_password.click_request_otp_button_email()
            forgot_password.clear_email()
            forgot_password.enter_email(Forgotpasswordtestdata.incorrect_email_2)
            forgot_password.click_request_otp_button_email()
            forgot_password.clear_email()
            forgot_password.enter_email(Forgotpasswordtestdata.incorrect_email_3)
            forgot_password.click_request_otp_button_email()
            forgot_password.clear_email()
            # Un-Registered E-mail Address:
            forgot_password.enter_email(Forgotpasswordtestdata.incorrect_email_4)
            forgot_password.click_request_otp_button_email()
            forgot_password.clear_email()
            # Empty:
            forgot_password.click_request_otp_button_email()
            time.sleep(3)
        except Exception as Forgot_password_email_validation_Error:
            print("Forgot password Error.", Forgot_password_email_validation_Error)

    @pytest.mark.id("TC-FP-003")
    def test_02_forgot_password_email_otp_validation(self):
        try:
            forgot_password = ForgotPasswordPage(self.driver)
            forgot_password.enter_email(Forgotpasswordtestdata.email)
            forgot_password.click_request_otp_button_email()
            # Incorrect OTP:
            forgot_password.enter_email_otp(Forgotpasswordtestdata.incorrect_OTP_1)
            forgot_password.click_email_otp_verify_button()
            forgot_password.clear_email_otp()
            forgot_password.enter_email_otp(Forgotpasswordtestdata.incorrect_OTP_2)
            forgot_password.click_email_otp_verify_button()
            forgot_password.clear_email_otp()
            forgot_password.enter_email_otp(Forgotpasswordtestdata.incorrect_OTP_3)
            forgot_password.click_email_otp_verify_button()
            forgot_password.clear_email_otp()
            # Expired OTP:
            forgot_password.fetch_email_otp_and_enter_email_otp()
            time.sleep(175)
            forgot_password.click_email_otp_verify_button()
            time.sleep(2)
            forgot_password.clear_email_otp()
            time.sleep(2)
        except Exception as forgot_password_email_otp_validation_Error:
            print("forgot_password_email_otp_validation_Error.", forgot_password_email_otp_validation_Error)

    @pytest.mark.id("TC-FP-007")
    def test_03_forgot_password_resend_email_otp_verify(self):
        try:
            forgot_password = ForgotPasswordPage(self.driver)
            forgot_password.click_resend_otp_link_email()
            forgot_password.fetch_email_otp_and_enter_email_otp()
            forgot_password.click_email_otp_verify_button()
            time.sleep(5)
        except Exception as forgot_password_resend_email_otp_Error:
            print("forgot_password_email_otp_validation_Error.", forgot_password_resend_email_otp_Error)

    @pytest.mark.id("TC-FP-004")
    def test_04_forgot_password_mobile_number_validation(self):
        try:
            forgot_password = ForgotPasswordPage(self.driver)
            """
            forgot_password.click_forgot_password_link()
            forgot_password.enter_email(Forgotpasswordtestdata.email)
            forgot_password.click_request_otp_button_email()
            forgot_password.fetch_email_otp_and_enter_email_otp()
            forgot_password.click_email_otp_verify_button()
            """
            # Invalid Mobile Number:
            forgot_password.enter_mobile_number(Forgotpasswordtestdata.incorrect_mobile_number_1)
            forgot_password.click_request_otp_button_mobile_number()
            forgot_password.clear_mobile_number()
            forgot_password.enter_mobile_number(Forgotpasswordtestdata.incorrect_mobile_number_2)
            forgot_password.click_request_otp_button_mobile_number()
            forgot_password.clear_mobile_number()
            forgot_password.enter_mobile_number(Forgotpasswordtestdata.incorrect_mobile_number_3)
            forgot_password.click_request_otp_button_mobile_number()
            forgot_password.clear_mobile_number()

            # Un-Registered Mobile-Number:
            forgot_password.enter_mobile_number(Forgotpasswordtestdata.Unregister_mobile_number)
            forgot_password.click_request_otp_button_mobile_number()
            forgot_password.clear_mobile_number()

            # Empty:
            forgot_password.click_request_otp_button_mobile_number()
            # self.driver.refresh()

        except Exception as forgot_password_resend_email_otp_Error:
            print("forgot_password_email_otp_validation_Error.", forgot_password_resend_email_otp_Error)

    @pytest.mark.id("TC-FP-005")
    def test_05_forgot_password_mobile_number_otp_validation(self):
        try:

            forgot_password = ForgotPasswordPage(self.driver)
            """
            forgot_password.click_forgot_password_link()
            
            forgot_password.enter_email(Forgotpasswordtestdata.email)
            forgot_password.click_request_otp_button_email()
            forgot_password.fetch_email_otp_and_enter_email_otp()
            forgot_password.click_email_otp_verify_button()
            """
            forgot_password.enter_mobile_number(Forgotpasswordtestdata.mobile_number)
            forgot_password.click_request_otp_button_mobile_number()

            # Incorrect OTP:
            forgot_password.enter_mobile_otp(Forgotpasswordtestdata.incorrect_OTP_1)
            forgot_password.click_mobile_otp_verify_button()
            forgot_password.clear_mobile_otp()
            forgot_password.enter_mobile_otp(Forgotpasswordtestdata.incorrect_OTP_2)
            forgot_password.click_mobile_otp_verify_button()
            forgot_password.clear_mobile_otp()
            forgot_password.enter_mobile_otp(Forgotpasswordtestdata.incorrect_OTP_3)
            forgot_password.click_mobile_otp_verify_button()
            forgot_password.clear_mobile_otp()
            time.sleep(3)
            # Expired OTP :
            forgot_password.fetch_mobile_otp_and_enter_mobile_otp()
            time.sleep(170)
            forgot_password.click_mobile_otp_verify_button()
            time.sleep(2)
            forgot_password.clear_mobile_otp()
            time.sleep(3)
        except Exception as forgot_password_mobile_number_otp_validation_Error:
            print("forgot_password_mobile_number_otp_validation_Error", forgot_password_mobile_number_otp_validation_Error)

    @pytest.mark.id("TC-FP-008")
    def test_06_forgot_password_resend_mobile_otp_verify(self):
        try:
            forgot_password = ForgotPasswordPage(self.driver)
            """
            forgot_password.click_forgot_password_link()

            forgot_password.enter_email(Forgotpasswordtestdata.email)
            forgot_password.click_request_otp_button_email()
            forgot_password.fetch_email_otp_and_enter_email_otp()
            forgot_password.click_email_otp_verify_button()

            forgot_password.enter_mobile_number(Forgotpasswordtestdata.mobile_number)
            forgot_password.click_request_otp_button_mobile_number()
            time.sleep(185)
            """
            forgot_password.click_resend_otp_link_mobile_number()
            forgot_password.fetch_mobile_otp_and_enter_mobile_otp()
            forgot_password.click_mobile_otp_verify_button()
            forgot_password.click_popup_ok_button()
            time.sleep(2)
        except Exception as forgot_password_resend_mobile_otp_verify:
            print("forgot_password_resend_mobile_otp_verify_Error", forgot_password_resend_mobile_otp_verify)

    @pytest.mark.id("TC-FP-001,TC-FP-009")
    def test_07_forgot_password(self):
        try:
            forgot_password = ForgotPasswordPage(self.driver)
            try:
                forgot_password.click_forgot_password_link()
            except:
                pass
            forgot_password.enter_email(Forgotpasswordtestdata.email)
            forgot_password.click_request_otp_button_email()
            forgot_password.fetch_email_otp_and_enter_email_otp()
            forgot_password.click_email_otp_verify_button()
            forgot_password.select_dropdown_option()
            forgot_password.select_india_dropdown_option()
            forgot_password.enter_mobile_number(Forgotpasswordtestdata.mobile_number)
            forgot_password.click_request_otp_button_mobile_number()
            forgot_password.fetch_mobile_otp_and_enter_mobile_otp()
            forgot_password.click_mobile_otp_verify_button()
            forgot_password.click_popup_ok_button()
            time.sleep(3)
        except Exception as Forgot_password_Error:
            print("Forgot password Error.", Forgot_password_Error)



