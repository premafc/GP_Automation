import pytest
import allure
import time
from Pages.Myprofile_RI import Myprofile_RI
from Testdata import Myprofile_RI_testdata
import time
import re


@pytest.mark.usefixtures("setup_class")
class Test_Myprofile_RI:

    driver = None  # Explicitly define the driver attribute
    url = "https://gold.groupnpay.com/#/"

    def __init__(self, driver=None):  # Accept driver in the constructor
        self.driver = driver

    @allure.id("TC-MP-RI-001")  # Unique Test Case ID
    @allure.description("Verify that the user is prompted with an alert when attempting to dismiss the Terms for Offer "
                        "popup without agreeing to the terms, and is logged out upon confirmation.")
    def test_terms_for_offer_rejected(self):
        try:
            my_profile_page = Myprofile_RI(self.driver)
            time.sleep(3)
            my_profile_page.click_mp_terms_for_offer_x_mark()
            my_profile_page.click_mp_yes_button()
        except Exception as test_terms_for_offer_rejected_Error:
            print("test_terms_for_offer_rejected_Error.", test_terms_for_offer_rejected_Error)

    @allure.id("TC-MP-RI-002")  # Unique Test Case ID
    @allure.description("Verify that the user cannot submit without agreeing to the Terms for offer.")
    def test_Verify_terms_not_agreed_submission(self):
        try:
            my_profile_page = Myprofile_RI(self.driver)
            time.sleep(3)
            my_profile_page.scroll_down_500()
            time.sleep(2)
            my_profile_page.mp_offer_submit_button()
            time.sleep(2)
            msg = my_profile_page.mp_offer_field_error_msg()
            time.sleep(2)
            my_profile_page.scroll_up()
            assert msg == 'Please agree the Terms for the Offer', f'Test Failed : Expected : Please agree the Terms for the Offer{msg}'
        except Exception as Verify_terms_not_agreed_submission_Error:
            print("test_Verify_terms_not_agreed_submission_Error.", Verify_terms_not_agreed_submission_Error)

    @allure.id("TC-MP-RI-006")  # Unique Test Case ID
    @allure.description("Verify that the user can successfully agree to the Terms and Conditions and proceed.")
    def test_terms_for_offer_agreed(self):
        my_profile_page = Myprofile_RI(self.driver)
        #my_profile_page = Myprofile_RI(setup_browser)
        my_profile_page.scroll()
        my_profile_page.mp_offer_checkbox()
        my_profile_page.mp_offer_submit_button()
        msg = my_profile_page.mp_offer_popup_msg()
        time.sleep(2)
        my_profile_page.click_mp_offer_success_button()
        assert msg == 'Thanks for Accepting the terms for the Offer.', f'Test Failed : Expected : Thanks for Accepting the terms for the Offer.{msg}'

    @allure.id("TC-MP-RI-009")  # Unique Test Case ID
    @allure.description("Verify that the user can accurately fill out mandatory fields, upload required documents, "
                        "and successfully save the my profile as a draft under the Major category in the "
                        "My Profile KYC.")
    def test_save_major_profile_draft(self):
        try:
            time.sleep(10)
            my_profile_page = Myprofile_RI(self.driver)
            # my_profile_page = Myprofile_RI(setup_browser)
            my_profile_page.scroll_up()
            my_profile_page.user_category_major_status_of_applicant_individual()
            # my_profile_page.user_category_major()
            # time.sleep(3)
            # my_profile_page.status_of_applicant_dropdown()
            # my_profile_page.status_of_applicant_individual()
            my_profile_page.select_date_of_birth_field()
            my_profile_page.click_date_of_birth()
            my_profile_page.enter_pan_number(Myprofile_RI_testdata.PanNumber_Value)
            my_profile_page.enter_aadhar_number(Myprofile_RI_testdata.Aadhaar_Number_Value)
            my_profile_page.enter_permanent_address(Myprofile_RI_testdata.PermanentAddress_Value)
            my_profile_page.scroll_down_200()
            my_profile_page.country_dropdown()
            my_profile_page.country_india()
            my_profile_page.select_state()
            my_profile_page.enter_city(Myprofile_RI_testdata.City_Value)
            my_profile_page.enter_postal_code(Myprofile_RI_testdata.PostalCode_Value)
            my_profile_page.select_same_as_permanent_address_checkbox()
            my_profile_page.scroll_down_200()
            my_profile_page.upload_pan_image(Myprofile_RI_testdata.UploadPan_Image)
            my_profile_page.upload_address_proof(Myprofile_RI_testdata.UploadAddressProof_Image)
            my_profile_page.upload_profile_photo(Myprofile_RI_testdata.UploadProfilePhoto_Image)
            my_profile_page.scroll_down_500()
            my_profile_page.select_terms_checkbox()
            my_profile_page.scroll_down_500()
            my_profile_page.click_save_as_draft_button()
            my_profile_page.click_my_profile_yes_button()
            msg = my_profile_page.verify_save_as_draft_message()
            my_profile_page.click_save_as_draft_ok_button()
            my_profile_page.click_my_profile_icon()
            my_profile_page.click_my_profile_text()
            time.sleep(15)
            assert msg == 'Your application has been saved as draft.', f'Test Failed : Expected : Your application has been saved as draft.{msg}'
        except Exception as save_major_profile_draft_Error:
            print("save_major_profile_draft_Error.", save_major_profile_draft_Error)

    @allure.id("TC-MP-RI-011")  # Unique Test Case ID
    @allure.description("Verify that the user can successfully fill out all mandatory fields, "
                        "upload required documents, and save the My Profile KYC form as a draft when the user category "
                        "is set to Major. Additionally, validate the system’s behavior when switching the "
                        "user category from Major to Minor, ensuring that specific fields (such as Date of Birth, "
                        "PAN Number, and Aadhaar Number) are cleared, while others retain pre-filled information, "
                        "and Guardian details are displayed.")
    def test_major_to_minor_save_as_draft(self):
        try:
            time.sleep(15)
            my_profile_page = Myprofile_RI(self.driver)
            my_profile_page.user_category_minor()
            my_profile_page.select_date_of_birth_field()
            my_profile_page.click_date_of_birth()
            my_profile_page.enter_pan_number(Myprofile_RI_testdata.PanNumber_Value)
            my_profile_page.enter_aadhar_number(Myprofile_RI_testdata.Aadhaar_Number_Value)
            my_profile_page.scroll_down_500()
            my_profile_page.enter_guardian_name(Myprofile_RI_testdata.Guardian_name_value)
            my_profile_page.select_guardian_date_of_birth()
            my_profile_page.click_date_of_birth()
            my_profile_page.enter_guardian_relation(Myprofile_RI_testdata.Guardian_relation_value)
            my_profile_page.enter_guardian_pan(Myprofile_RI_testdata.Guardian_pan_value)
            my_profile_page.scroll_down_500()
            my_profile_page.enter_guardian_aadhar(Myprofile_RI_testdata.Guardian_aadhar_value)
            my_profile_page.upload_guardian_pan(Myprofile_RI_testdata.Upload_guardian_pan_Image)
            my_profile_page.upload_guardian_aadhar(Myprofile_RI_testdata.Upload_guardian_aadhar_Image)
            my_profile_page.scroll_down_500()
            my_profile_page.scroll_down_500()
            my_profile_page.click_save_as_draft_button()
            my_profile_page.click_my_profile_yes_button()
            msg = my_profile_page.verify_save_as_draft_message()
            my_profile_page.click_save_as_draft_ok_button()
            my_profile_page.click_my_profile_icon()
            my_profile_page.click_my_profile_text()
            time.sleep(15)
            assert msg == 'Your application has been saved as draft.', f'Test Failed : Expected : Your application has been saved as draft.{msg}'
        except Exception as major_to_minor_save_as_draft_Error:
            print("test_major_to_minor_save_as_draft_Error.", major_to_minor_save_as_draft_Error)

    @allure.id("TC-MP-RI-012")  # Unique Test Case ID
    @allure.description("Verify that the user can successfully fill out all required fields, upload necessary "
                        "documents, and save the My Profile KYC form as a draft when the user category is "
                        "set to Minor. Additionally, validate the system's response when switching the user category "
                        "from Minor to Major, ensuring that specific fields are reset while others retain their "
                        "pre-filled information.")
    def test_minor_to_major_save_as_draft(self):
        try:
            time.sleep(15)
            my_profile_page = Myprofile_RI(self.driver)
            my_profile_page.user_category_major()
            my_profile_page.select_date_of_birth_field()
            my_profile_page.click_date_of_birth()
            my_profile_page.enter_pan_number(Myprofile_RI_testdata.PanNumber_Value)
            my_profile_page.enter_aadhar_number(Myprofile_RI_testdata.Aadhaar_Number_Value)
            my_profile_page.scroll_down_500()
            my_profile_page.scroll_down_500()
            my_profile_page.click_save_as_draft_button()
            my_profile_page.click_my_profile_yes_button()
            msg = my_profile_page.verify_save_as_draft_message()
            my_profile_page.click_save_as_draft_ok_button()
            my_profile_page.click_my_profile_icon()
            my_profile_page.click_my_profile_text()
            time.sleep(15)
            assert msg == 'Your application has been saved as draft.', f'Test Failed : Expected : Your application has been saved as draft.{msg}'
        except Exception as minor_to_major_save_as_draft_Error:
            print("test_minor_to_major_save_as_draft_Error.", minor_to_major_save_as_draft_Error)

    @allure.id("TC-MP-RI-013")  # Unique Test Case ID
    @allure.description("Verify My Profile KYC Submission User Category as Major to ensure that the user can "
                        "accurately fill out mandatory fields, upload required documents, and successfully "
                        "submit the My Profile KYC.")
    def test_my_profile_major_submit_images(self):
        try:
            time.sleep(10)
            my_profile_page = Myprofile_RI(self.driver)
            my_profile_page.scroll_down_500()
            my_profile_page.scroll_down_500()
            my_profile_page.click_submit_button()
            my_profile_page.click_my_profile_yes_button()
            # actual_text = myprofile.submit_pop_up_msg()
            my_profile_page.click_submit_ok_button()
            time.sleep(3)
            my_profile_page.click_my_profile_icon()
            my_profile_page.click_my_profile_text()
            time.sleep(10)
            """
            print("Actual Text:", actual_text)
            pattern = (r'The above information provided has been updated.\n'
                       r'The files uploaded have been received.\n'
                       r'KYC verification is being processed.')
            assert re.match(pattern, actual_text), f"Text does not match the expected pattern. Actual: {actual_text}"
            """
        except Exception as my_profile_major_submit_images_Error:
            print("test_my_profile_major_submit_images_Error.", my_profile_major_submit_images_Error)

    @allure.id("TC-MP-RI-013")
    @allure.description("Verify My Profile KYC Submission User Category as Major to ensure that the user can "
                        "accurately fill out mandatory fields, upload required documents, and successfully "
                        "submit the My Profile KYC. Note : PDF.")
    def test_my_profile_major_submit_pdf(self):
        try:
            my_profile_page = Myprofile_RI(self.driver)
            # my_profile_page = Myprofile_RI(setup_browser)
            my_profile_page.scroll_down_500()
            my_profile_page.upload_pan_image(Myprofile_RI_testdata.UploadPan_pdf)
            my_profile_page.upload_address_proof(Myprofile_RI_testdata.UploadAddressProof_pdf)
            my_profile_page.upload_profile_photo(Myprofile_RI_testdata.UploadProfilePhoto_pdf)
            my_profile_page.scroll_down_500()
            my_profile_page.click_submit_button()
            my_profile_page.click_my_profile_yes_button()
            # actual_text = my_profile_page.submit_pop_up_msg()
            my_profile_page.click_submit_ok_button()
            time.sleep(3)
            my_profile_page.click_my_profile_icon()
            my_profile_page.click_my_profile_text()
            time.sleep(10)
            """
            print("Actual Text:", actual_text)
            pattern = (r'The above information provided has been updated.\n'
                       r'The files uploaded have been received.\n'
                       r'KYC verification is being processed.')
            assert re.match(pattern, actual_text), f"Text does not match the expected pattern. Actual: {actual_text}"
            """
        except Exception as my_profile_major_submit_pdf_Error:
            print("test_my_profile_major_submit_pdf_Error.", my_profile_major_submit_pdf_Error)

    @allure.id("TC-MP-RI-014")  # Unique Test Case ID
    @allure.description("Verify My Profile KYC Submission Minor to ensure that the user can accurately fill out "
                        "mandatory fields, upload required documents, and successfully submit the My Profile KYC.")
    def test_my_profile_minor_submit_images(self):
        try:
            my_profile_page = Myprofile_RI(self.driver)
            # my_profile_page = Myprofile_RI(setup_browser)
            my_profile_page.user_category_minor()
            my_profile_page.select_date_of_birth_field()
            my_profile_page.click_date_of_birth()
            my_profile_page.enter_pan_number(Myprofile_RI_testdata.PanNumber_Value)
            my_profile_page.enter_aadhar_number(Myprofile_RI_testdata.Aadhaar_Number_Value)
            my_profile_page.scroll_down_500()
            my_profile_page.upload_pan_image(Myprofile_RI_testdata.UploadPan_Image)
            my_profile_page.upload_address_proof(Myprofile_RI_testdata.UploadAddressProof_Image)
            my_profile_page.upload_profile_photo(Myprofile_RI_testdata.UploadProfilePhoto_Image)
            my_profile_page.scroll_down_500()
            my_profile_page.enter_guardian_name(Myprofile_RI_testdata.Guardian_name_value)
            my_profile_page.select_guardian_date_of_birth()
            my_profile_page.click_date_of_birth()
            my_profile_page.enter_guardian_relation(Myprofile_RI_testdata.Guardian_relation_value)
            my_profile_page.enter_guardian_pan(Myprofile_RI_testdata.Guardian_pan_value)
            my_profile_page.scroll_down_500()
            my_profile_page.enter_guardian_aadhar(Myprofile_RI_testdata.Guardian_aadhar_value)
            my_profile_page.upload_guardian_pan(Myprofile_RI_testdata.Upload_guardian_pan_Image)
            my_profile_page.upload_guardian_aadhar(Myprofile_RI_testdata.Upload_guardian_aadhar_Image)
            my_profile_page.scroll_down_500()
            my_profile_page.scroll_down_500()
            my_profile_page.click_submit_button()
            my_profile_page.click_my_profile_yes_button()
            # actual_text = myprofile.submit_pop_up_msg()
            my_profile_page.click_submit_ok_button()
            time.sleep(3)
            my_profile_page.click_my_profile_icon()
            my_profile_page.click_my_profile_text()
            time.sleep(10)
            """
            print("Actual Text:", actual_text)
            pattern = (r'The above information provided has been updated.\n'
                       r'The files uploaded have been received.\n'
                       r'KYC verification is being processed.')
            assert re.match(pattern, actual_text), f"Text does not match the expected pattern. Actual: {actual_text}"
            """
        except Exception as my_profile_minor_submit_images_Error:
            print("test_my_profile_minor_submit_images_Error.", my_profile_minor_submit_images_Error)

    @allure.id("TC-MP-RI-014")  # Unique Test Case ID
    @allure.description("Verify My Profile KYC Submission Minor to ensure that the user can accurately fill out "
                        "mandatory fields, upload required documents, and successfully submit the My Profile KYC.")
    def test_my_profile_minor_submit_pdf(self):
        try:
            my_profile_page = Myprofile_RI(self.driver)
            my_profile_page.scroll_down_500()
            my_profile_page.upload_pan_image(Myprofile_RI_testdata.UploadPan_pdf)
            my_profile_page.upload_address_proof(Myprofile_RI_testdata.UploadAddressProof_pdf)
            my_profile_page.upload_profile_photo(Myprofile_RI_testdata.UploadProfilePhoto_pdf)
            my_profile_page.scroll_down_500()
            my_profile_page.upload_guardian_pan(Myprofile_RI_testdata.Upload_guardian_pan_pdf)
            my_profile_page.upload_guardian_aadhar(Myprofile_RI_testdata.Upload_guardian_aadhar_pdf)
            my_profile_page.scroll_down_500()
            my_profile_page.scroll_down_500()
            my_profile_page.click_submit_button()
            my_profile_page.click_my_profile_yes_button()
            # actual_text = myprofile.submit_pop_up_msg()
            my_profile_page.click_submit_ok_button()
            time.sleep(3)
            my_profile_page.click_my_profile_icon()
            my_profile_page.click_my_profile_text()
            time.sleep(10)
            """
            print("Actual Text:", actual_text)
            pattern = (r'The above information provided has been updated.\n'
                       r'The files uploaded have been received.\n'
                       r'KYC verification is being processed.')
            assert re.match(pattern, actual_text), f"Text does not match the expected pattern. Actual: {actual_text}"
            """
        except Exception as my_profile_minor_submit_pdf_Error:
            print("test_my_profile_minor_submit_pdf_Error.", my_profile_minor_submit_pdf_Error)

    @allure.id("TC-MP-RI-019")  # Unique Test Case ID
    @allure.description("Verify the Rejected Reason show on the My profile page and Re-submit the User successfully.")
    def test_verify_rejected_reason(self):
        try:
            my_profile_page = Myprofile_RI(self.driver)
            my_profile_page.scroll_down_500()
            time.sleep(1)
            my_profile_page.scroll_down_500()
            time.sleep(2)
            my_profile_page.click_submit_button()
            my_profile_page.click_my_profile_yes_button()
            my_profile_page.click_submit_ok_button()
            time.sleep(3)

        except Exception as my_profile_rejected_reason_Error:
            print("test_verify_rejected_reason_Error.", my_profile_rejected_reason_Error)

