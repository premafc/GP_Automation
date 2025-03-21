import pytest
import allure
import time
from Pages.Investor_KYC_Details import Investor_KYC_Details
from Locators import Investor_kyc_details_locators
from Testdata import logintestdata
from Pages.Myprofile_RI import Myprofile_RI
import time
import re

@pytest.mark.usefixtures("setup_class")
class Test_Investor_KYC_Details:

    driver = None  # Explicitly define the driver attribute
    url = "https://gold.groupnpay.com/#/"

    def test_Logout(self):
        obj_Investor_KYC_Details = Investor_KYC_Details(self.driver)
        # obj_Investor_KYC_Details.Investor_KYC_details()
        obj_Investor_KYC_Details.profile_icon()
        obj_Investor_KYC_Details.approver_logout()

    def test_KYC_Reject(self):
        obj_Investor_KYC_Details = Investor_KYC_Details(self.driver)
        obj_Investor_KYC_Details.Investor_KYC_details()
        obj_Investor_KYC_Details.Search_field(logintestdata.valid_username)
        time.sleep(2)
        obj_Investor_KYC_Details.view_button()
        obj_Investor_KYC_Details.scroll_down()
        obj_Investor_KYC_Details.KYC_Remarks_Checkbox()
        obj_Investor_KYC_Details.KYC_Remarks(Investor_kyc_details_locators.KYC_Rejected_Reason)
        obj_Investor_KYC_Details.submit_button()
        obj_Investor_KYC_Details.yes_button()
        msg = obj_Investor_KYC_Details.Kyc_rejected_pop_up_msg()
        obj_Investor_KYC_Details.OK_pop_up()
        obj_Investor_KYC_Details.dropdown_Investor_KYC_details()
        obj_Investor_KYC_Details.dropdown_rejected()
        obj_Investor_KYC_Details.Search_field(logintestdata.valid_username)
        obj_Investor_KYC_Details.view_button()
        obj_Investor_KYC_Details.scroll_down()
        assert msg == 'KYC details are not compliant. Queries have been sent to your registered email id.', f'Test Failed : Expected : KYC details are not compliant. Queries have been sent to your registered email id.'

    def test_KYC_Approve(self):
        try:
            obj_Investor_KYC_Details = Investor_KYC_Details(self.driver)
            obj_Investor_KYC_Details.Investor_KYC_details()
            obj_Investor_KYC_Details.Search_field(logintestdata.valid_username)
            obj_Investor_KYC_Details.view_button()
            obj_Investor_KYC_Details.scroll_down()
            obj_Investor_KYC_Details.KYC_Agreed_Checkbox()
            obj_Investor_KYC_Details.submit_button()
            obj_Investor_KYC_Details.yes_button()
            msg = obj_Investor_KYC_Details.Kyc_approved_pop_up_msg()
            obj_Investor_KYC_Details.OK_pop_up()
            obj_Investor_KYC_Details.dropdown_Investor_KYC_details()
            obj_Investor_KYC_Details.dropdown_approved()
            obj_Investor_KYC_Details.Search_field(logintestdata.valid_username)
            obj_Investor_KYC_Details.view_button()
            obj_Investor_KYC_Details.scroll_down()

            assert msg == 'User KYC Verified.', f'Test Failed : Expected : User KYC Verified.'

        except Exception as KYC_Approved_Error:
            print("KYC Approved Error.", KYC_Approved_Error)

