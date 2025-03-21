import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Investor_kyc_details_locators

class Investor_KYC_Details:

    def __init__(self, driver):
        self.driver = driver

    def Investor_KYC_details(self):
        kyc_details = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Investor_KYC_details))
        )
        kyc_details.click()

    def Search_field(self, Username):
        time.sleep(1)
        search_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Search))
        )
        search_field.send_keys(Username)
        time.sleep(2)

    def Search_field_x_mark(self):
        search_field_x_mark_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Search_X_mark))
        )
        search_field_x_mark_button.click()

    def view_button(self):
        investor_kyc_view_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.View_button))
        )
        investor_kyc_view_button.click()
        time.sleep(5)

    def KYC_Remarks_Checkbox(self):
        kyc_remarks_check_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Kyc_remarks_checkbox))
        )
        kyc_remarks_check_box.click()

    def KYC_Remarks(self, KYC_Rejected_Reason_value):
        kyc_remarks = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Remarks_Entered_box))
        )
        kyc_remarks.send_keys(KYC_Rejected_Reason_value)

    def KYC_Agreed_Checkbox(self):
        kyc_agreed_check_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Agree_check_box))
        )
        kyc_agreed_check_box.click()

    def submit_button(self):
        submit = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Submit_button))
        )
        submit.click()

    def yes_button(self):
        yes = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Yes_button))
        )
        yes.click()

    def no_button(self):
        no = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.No_button))
        )
        no.click()

    def OK_pop_up(self):
        time.sleep(1)
        ok_pop_up = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.OK_Pop_UP))
        )
        ok_pop_up.click()

    def profile_icon(self):
        time.sleep(3)
        profile_icon_approver = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.my_profile_icon))
        )
        profile_icon_approver.click()

    def approver_logout(self):
        time.sleep(2)
        logout = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.approver_logout))
        )
        logout.click()

    def dropdown_Investor_KYC_details(self):
        time.sleep(2)
        dropdown = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.dropdown_KYC))
        )
        dropdown.click()

    def dropdown_approval_pending(self):
        approval_pending = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Approval_pending_dropdown))
        )
        approval_pending.click()

    def dropdown_approved(self):
        approved = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Approved_dropdown))
        )
        approved.click()

    def dropdown_rejected(self):
        rejected = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.Rejected_dropdown))
        )
        rejected.click()

    def Kyc_rejected_pop_up_msg(self):
        time.sleep(2)
        rejected_pop_up_msg = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.KYC_Rejected_Pop_Up_Msg))
        )
        log = rejected_pop_up_msg.text
        print(log)
        return log

    def Kyc_approved_pop_up_msg(self):
        time.sleep(2)
        approved_pop_up_msg = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.KYC_Approved_Pop_Up_Msg))
        )
        log = approved_pop_up_msg.text
        print(log)
        return log

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def my_profile_icon(self):
        time.sleep(2)
        # My profile Icon
        MyProfile_Icon = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.my_profile_icon))
        )
        MyProfile_Icon.click()

    def my_logout_text(self):
        # logout
        time.sleep(2)
        logout = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Investor_kyc_details_locators.logout_text))
        )
        logout.click()

