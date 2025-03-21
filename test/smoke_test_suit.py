import pytest
from test_Loginpage import TestLogin
from test_Myprofile_RI import Test_Myprofile_RI
from test_Investor_KYC_Details import Test_Investor_KYC_Details
import allure
from allure_commons.types import AttachmentType

@pytest.mark.usefixtures("setup_class")  # Use the setup_class fixture for initialization
class Test_Suite_Smoke:
    driver =None

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.id("TC-Login-001")
    @pytest.mark.description("valid login functionality.")
    def test_valid_login(self):
        login_test = TestLogin()
        login_test.driver = self.driver
        login_test.test_login()  # Run the login test

    @pytest.mark.id("TC-MP-RI-005")
    def test_terms_for_offer_agreed(self):
        myprofile_test = Test_Myprofile_RI()
        myprofile_test.driver = self.driver
        myprofile_test.test_terms_for_offer_agreed()

    @pytest.mark.id("TC-MP-RI-009")
    def test_save_major_profile_draft(self):
        myprofile_test = Test_Myprofile_RI()
        myprofile_test.driver = self.driver
        myprofile_test.test_save_major_profile_draft()

    @pytest.mark.id("TC-MP-RI-013")
    def test_my_profile_major_submit(self):
        myprofile_test = Test_Myprofile_RI()
        myprofile_test.driver = self.driver
        myprofile_test.test_my_profile_major_submit_pdf()

    @pytest.mark.id("TC-User_logout-001")
    def test_user_logout(self):
        login_test = TestLogin(self.driver)
        login_test.test_user_logout()

    @pytest.mark.id("TC-Investor-KYC-Details - 001")
    def test_approver_login(self):
        test_login = TestLogin()
        test_login.driver = self.driver
        test_login.test_approver_login()

    @pytest.mark.id("TC-Investor-KYC-Details - 004")
    def test_kyc_rejected(self):
        investor_kyc_details_test = Test_Investor_KYC_Details()
        investor_kyc_details_test.driver = self.driver
        investor_kyc_details_test.test_KYC_Reject()

    @pytest.mark.id("TC-approver_logout-001")
    def test_approver_logout(self):
        investor_kyc_details_test = Test_Investor_KYC_Details()
        investor_kyc_details_test.driver = self.driver
        investor_kyc_details_test.test_Logout()

    @pytest.mark.id("TC-MP-RI-018")
    def test_verify_rejected_reason(self):
        # Login with Investor Verify the Rejected Reason on MY profile.
        login_test = TestLogin()
        login_test.driver = self.driver  # Use the shared driver
        login_test.test_login()  # Run the login test
        # Verify the Rejected Reason:
        my_profile_test = Test_Myprofile_RI()
        my_profile_test.driver = self.driver
        my_profile_test.test_verify_rejected_reason()
        # User Logout:
        login_test = TestLogin(self.driver)
        login_test.driver = self.driver
        login_test.test_user_logout()

    @pytest.mark.id("TC-Investor-KYC-Details - 005")
    def test_investor_kyc_approved(self):
        # Approver Login :
        login_test = TestLogin()
        login_test.driver = self.driver
        login_test.test_approver_login()
        # Investor KYC Details Approved :
        investor_kyc_details_test = Test_Investor_KYC_Details()
        investor_kyc_details_test.driver = self.driver
        investor_kyc_details_test.test_KYC_Approve()
        # Approver Logout :
        investor_kyc_details_test.test_Logout()



