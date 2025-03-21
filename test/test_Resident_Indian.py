import pytest
from test_Loginpage import TestLogin
from test_Myprofile_RI import Test_Myprofile_RI
from test_Investor_KYC_Details import Test_Investor_KYC_Details

@pytest.mark.usefixtures("setup_class")
class TestEndFile:
    driver = None  # WebDriver instance

    @pytest.mark.id("TC-Login-002")
    @pytest.mark.description("Invalid login functionality.")
    def test_invalid_login(self):
        login_test = TestLogin()
        login_test.driver = self.driver
        login_test.test_invalid_login()

    @pytest.mark.id("TC-Login-004")
    @pytest.mark.description("Test locked GP-Account. More than 3 times tried.")
    def test_locked_account(self):
        login_test = TestLogin()
        login_test.driver = self.driver
        login_test.test_locked_account()

    @pytest.mark.id("TC-Login-008")
    @pytest.mark.description("Test SQL Injection.")
    def test_sql_injection(self):
        login_test = TestLogin()
        login_test.driver = self.driver
        login_test.test_sql_injection()

    @pytest.mark.id("TC-Login-001")
    @pytest.mark.description("valid login functionality.")
    def test_valid_login(self):
        login_test = TestLogin()
        login_test.driver = self.driver
        login_test.test_login()

    @pytest.mark.id("TC-MP-RI-001")
    @pytest.mark.description("Validate the MY Profile Terms for offer Rejected.")
    def test_terms_for_offer_rejected(self):
        my_profile_test = Test_Myprofile_RI(self.driver)
        my_profile_test.driver = self.driver
        my_profile_test.test_terms_for_offer_rejected()
        # RE- Login with Valid Credentials.
        login_test = TestLogin()
        login_test.driver = self.driver
        login_test.test_login()

    @pytest.mark.id("TC-MP-RI-002")
    @pytest.mark.description("Validate the MY Profile Terms for offer check box not agreed.")
    def test_verify_terms_not_agreed_submission(self):
        my_profile_test = Test_Myprofile_RI(self.driver)
        my_profile_test.driver = self.driver
        my_profile_test.test_Verify_terms_not_agreed_submission()

    @pytest.mark.id("TC-MP-RI-006")
    @pytest.mark.description("Validate the MY Profile Terms for offer agreed.")
    def test_terms_for_offer_agreed(self):
        my_profile_test = Test_Myprofile_RI(self.driver)
        my_profile_test.driver = self.driver
        my_profile_test.test_terms_for_offer_agreed()

    @pytest.mark.id("TC-MP-RI-009")
    @pytest.mark.description("MY Profile KYC Submission Save as draft. Major.")
    def test_save_major_profile_draft(self):
        my_profile_test = Test_Myprofile_RI()
        my_profile_test.driver = self.driver
        my_profile_test.test_save_major_profile_draft()

    @pytest.mark.id("TC-MP-RI-011")
    @pytest.mark.description("MY Profile KYC Submission Save as draft. Major to Minor.")
    def test_major_to_minor_save_as_draft(self):
        my_profile_test = Test_Myprofile_RI()
        my_profile_test.driver = self.driver
        my_profile_test.test_major_to_minor_save_as_draft()

    @pytest.mark.id("TC-MP-RI-012")
    @pytest.mark.description("MY Profile KYC Submission Save as draft. Minor to Major.")
    def test_minor_to_major_save_as_draft(self):
        my_profile_test = Test_Myprofile_RI()
        my_profile_test.driver = self.driver
        my_profile_test.test_minor_to_major_save_as_draft()

    @pytest.mark.id("TC-MP-RI-013")
    @pytest.mark.description("MY Profile KYC Major Submit images.")
    def test_my_profile_major_submit_images(self):
        my_profile_test = Test_Myprofile_RI()
        my_profile_test.driver = self.driver
        my_profile_test.test_my_profile_major_submit_images()

    @pytest.mark.id("TC-MP-RI-013")
    @pytest.mark.description("MY Profile KYC Major Submit pdf.")
    def test_my_profile_major_submit_pdf(self):
        my_profile_test = Test_Myprofile_RI()
        my_profile_test.driver = self.driver
        my_profile_test.test_my_profile_major_submit_pdf()

    @pytest.mark.id("TC-MP-RI-014")
    @pytest.mark.description("MY Profile KYC Minor Submit images.")
    def test_my_profile_minor_submit_images(self):
        my_profile_test = Test_Myprofile_RI()
        my_profile_test.driver = self.driver
        my_profile_test.test_my_profile_minor_submit_images()

    @pytest.mark.id("TC-MP-RI-014")
    @pytest.mark.description("MY Profile KYC Minor Submit Pdf.")
    def test_my_profile_minor_submit_pdf(self):
        my_profile_test = Test_Myprofile_RI()
        my_profile_test.driver = self.driver
        my_profile_test.test_my_profile_minor_submit_pdf()

    @pytest.mark.id("TC-User_logout-001")
    @pytest.mark.description("Validate the User logout successfully.")
    def test_user_logout(self):
        login_test = TestLogin(self.driver)
        login_test.test_user_logout()

    @pytest.mark.id("TC-Investor-KYC-Details - 001")
    @pytest.mark.description("Validate the Application Approver login successfully.")
    def test_approver_login(self):
        test_login = TestLogin()
        test_login.driver = self.driver
        test_login.test_approver_login()

    @pytest.mark.id("TC-Investor-KYC-Details - 004")
    @pytest.mark.description("Validate the Application Approver KYC Rejected successfully.")
    def test_kyc_rejected(self):
        investor_kyc_details_test = Test_Investor_KYC_Details()
        investor_kyc_details_test.driver = self.driver
        investor_kyc_details_test.test_KYC_Reject()

    @pytest.mark.id("TC-approver_logout-001")
    @pytest.mark.description("Validate the Application Approver logout successfully.")
    def test_approver_logout(self):
        investor_kyc_details_test = Test_Investor_KYC_Details()
        investor_kyc_details_test.driver = self.driver
        investor_kyc_details_test.test_Logout()

    @pytest.mark.id("TC-MP-RI-018")
    @pytest.mark.description("Validate the MY Profile KYC Rejected Reason and Re-submit successfully.")
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
    @pytest.mark.description("Validate the Application Approver Approved the Investor KYC.")
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

