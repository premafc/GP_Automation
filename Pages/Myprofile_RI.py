import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Myprofile_RI_locators
from Testdata import Myprofile_RI_testdata

class Myprofile_RI:

    def __init__(self, driver):
        self.driver = driver

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def mp_offer_checkbox(self):
        mp_offer_check_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.MP_Terms_and_Offer))
        )
        mp_offer_check_box.click()

    def mp_offer_submit_button(self):
        # My profile : pop up Terms for the offer Submit button.
        mp_offer_submit = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.MP_Submit1))
        )
        mp_offer_submit.click()

    def mp_offer_field_error_msg(self):
        time.sleep(2)
        mp_pop_up_msg = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Terms_for_offer_error_message))
        )
        log = mp_pop_up_msg.text
        print(log)
        return log

    def mp_offer_popup_msg(self):
        mp_pop_up_msg = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[text() ='Thanks for Accepting the terms for the Offer.']"))
        )
        log = mp_pop_up_msg.text
        print(log)
        return log

    def click_mp_offer_success_button(self):
        # My profile : pop up Success ok button.
        mp_success = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Success))
        )
        mp_success.click()

    def click_mp_terms_for_offer_x_mark(self):
        # My profile : Terms for the offer X mark:
        x_mark_button = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Myprofile_RI_locators.X_Mark_Terms_and_offer))
        )
        x_mark_button.click()

    def click_mp_yes_button(self):
        # My profile : Pop up Yes button:
        yes_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.MP_Alert_Yes))
        )
        yes_button.click()

    def user_category_major_status_of_applicant_individual(self):
        # My profile Status of applicant field drop down using javascript.
        dropdown = self.driver.find_elements(By.CSS_SELECTOR, '.css-1xc3v61-indicatorContainer')
        dropdown[0].click()

        time.sleep(2)
        # Wait for the first option to be clickable and click it
        option_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Myprofile_RI_locators.Major))
        )
        option_element.click()

        time.sleep(3)
        dropdown[1].click()
        option_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Myprofile_RI_locators.Individual))
        )
        option_element.click()

    def user_category_minor(self):
        # My profile Status of applicant field drop down using javascript.
        dropdown = self.driver.find_elements(By.CSS_SELECTOR,'.css-1xc3v61-indicatorContainer')
        dropdown[0].click()

        time.sleep(2)
        # Wait for the first option to be clickable and click it
        option_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Myprofile_RI_locators.Minor))
        )
        option_element.click()
        time.sleep(2)

    def user_category_major(self):
        # My profile Status of applicant field drop down using javascript.
        dropdown = self.driver.find_elements(By.CSS_SELECTOR, '.css-1xc3v61-indicatorContainer')
        dropdown[0].click()
        time.sleep(2)
        # Wait for the first option to be clickable and click it
        option_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Myprofile_RI_locators.Major))
        )
        option_element.click()

    def status_of_applicant_dropdown(self):
        time.sleep(5)
        """
        # My profile Status of applicant field drop down using javascript.
        dropdown = self.driver.find_elements(By.CSS_SELECTOR, Myprofile_RI_locators.Status_of_Applicant)
        dropdown[1].click()
        """

    def status_of_applicant_individual(self):
        time.sleep(2)
        option_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Myprofile_RI_locators.Individual))
        )
        option_element.click()

    def select_date_of_birth_field(self):
        # Date of birth field:
        date_of_birth_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Date_of_Birth))
        )
        date_of_birth_field.click()

    def click_date_of_birth(self):
        # Date of birth field date:
        date_of_birth_field_date = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Date_month))
        )
        date_of_birth_field_date.click()

    def enter_pan_number(self,pan_number_value):
        # My profile Pan Number field.
        pan_number_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.PanNumber))
        )
        pan_number_field.send_keys(pan_number_value)

    def enter_aadhar_number(self, aadhar_number):
        # My profile Aadhar Number field.
        aadhar_number_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Aadhaar_Number))
        )
        aadhar_number_field.send_keys(aadhar_number)

    def enter_permanent_address(self,permanent_address):
        # My profile Permanent Address field.
        permanent_address_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.PermanentAddress))
        )
        permanent_address_field.send_keys(permanent_address)

    def country_dropdown(self,):
        time.sleep(2)
        # My profile Country drop down using javascript.
        dropdown = self.driver.find_elements(By.CSS_SELECTOR, '.css-1xc3v61-indicatorContainer')
        dropdown[2].click()
        time.sleep(2)

    def country_india(self):
        time.sleep(2)
        # Wait for the first option to be clickable and click it
        india_option = self.driver.find_element(By.XPATH, "//*[text()='INDIA']")
        self.driver.execute_script("arguments[0].click();", india_option)
        # Current update selenium is not identified in this element, So we will do using javascript.
        """
        option_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Myprofile_RI_locators.India1))
        )
        option_element.click()
        """
        time.sleep(3)

    def select_state(self):
        # My profile State drop down using javascript.
        dropdown = self.driver.find_elements(By.CSS_SELECTOR, '.css-1xc3v61-indicatorContainer')
        dropdown[2].click()
        time.sleep(2)
        # Wait for the first option to be clickable and click it
        option_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, Myprofile_RI_locators.State1))
        )
        option_element.click()

    def enter_city(self, city):
        # My profile City field.(PA)
        city_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.City1))
        )
        city_field.send_keys(city)

    def enter_postal_code(self,postal_code):
        # My profile PostalCode field.(PA)
        postalcode_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.PostalCode1))
        )
        postalcode_field.send_keys(postal_code)

    def select_same_as_permanent_address_checkbox(self):
        # My profile Same permanent Address checkbox
        pa_checkbox = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Same_as_permanentAddress))
        )
        pa_checkbox.click()

    def scroll_down_200(self):
        # Page window scroll down:
        self.driver.execute_script("window.scrollBy(0, 200);")

    def upload_pan_image(self, upload_pan):
        pan = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.UploadPan))
        )
        pan.send_keys(upload_pan)

    def upload_address_proof(self, upload_address_proof):
        # My profile address_proof
        address_proof = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.UploadAddressProof))
        )
        address_proof.send_keys(upload_address_proof)

    def upload_profile_photo(self,profile_image):
        # My profile profile photo
        profile_photo = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.UploadProfilePhoto))
        )
        profile_photo.send_keys(profile_image)

    def scroll_down_500(self):
        # Page window scroll down:
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)

    def select_terms_checkbox(self):
        # My profile Terms and conditions checkbox
        terms_checkbox = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Terms_and_conditions))
        )
        terms_checkbox.click()
        time.sleep(2)

    def click_save_as_draft_button(self):
        time.sleep(2)
        # My profile Save as draft button:
        save_as_draft_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Save_as_draft))
        )
        save_as_draft_button.click()

    def click_my_profile_yes_button(self):
        # My profile Yes button:
        Yes_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.MP_Confirmation_Yes))
        )
        Yes_button.click()

    def verify_save_as_draft_message(self):
        # Draft Pop Up message :
        mp_pop_up_msg = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[text() ='Your application has been saved as draft.']"))
        )
        log = mp_pop_up_msg.text
        print(log)
        return log

    def click_save_as_draft_ok_button(self):
        time.sleep(2)
        # My profile OK button:
        ok_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Ok_button))
        )
        ok_button.click()

    def enter_guardian_name(self,guardian_name):
        # My profile Guardian name
        guardian_name_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Guardian_name))
        )
        guardian_name_field.send_keys(guardian_name)

    def select_guardian_date_of_birth(self):
        # Date of birth field:
        guardian_date_of_birth_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Guardian_date_of_birth))
        )
        guardian_date_of_birth_field.click()

    def enter_guardian_relation(self, guardian_relation):
        # My profile Guardian Relation
        guardian_relation_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Guardian_relation))
        )
        guardian_relation_field.send_keys(guardian_relation)

    def enter_guardian_pan(self,guardian_pan):
        # My profile Guardian Pan
        guardian_pan_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Guardian_pan))
        )
        guardian_pan_field.send_keys(guardian_pan)

    def enter_guardian_aadhar(self, guardian_aadhar):
        # My profile Guardian aadhar
        guardian_aadhar_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Guardian_aadhar))
        )
        guardian_aadhar_field.send_keys(guardian_aadhar)

    def upload_guardian_pan(self, guardian_pan_image):
        # My profile Guardian pan image.
        upload_guardian_pan_ = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Upload_guardian_pan))
        )
        upload_guardian_pan_.send_keys(guardian_pan_image)

    def upload_guardian_aadhar(self, guardian_aadhar_image):
        # My profile Guardian aadhar
        upload_guardian_aadhar_ = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Upload_guardian_aadhar))
        )
        upload_guardian_aadhar_.send_keys(guardian_aadhar_image)

    def click_submit_button(self):
        # My profile submit button
        submit_button_ = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.MP_Submit2))
        )
        submit_button_.click()

    def click_my_profile_icon(self):
        time.sleep(2)
        # My profile Icon
        MyProfile_Icon = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.my_profile_icon))
        )
        MyProfile_Icon.click()

    def click_my_profile_text(self):
        # My profile Icon
        time.sleep(2)
        MyProfile = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.my_profile))
        )
        MyProfile.click()

    def submit_pop_up_msg(self):
        time.sleep(2)
        mp_pop_up_msg = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.submit_pop_up_msg))
        )
        log = mp_pop_up_msg.text
        print(log)
        return log

    def click_submit_ok_button(self):
        # My profile OK button:
        ok_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="modal_btn SUCCESS"]'))
        )
        ok_button.click()
        time.sleep(2)

    def mp_rejected_reason(self):
        mp_rejected_reason_msg = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, Myprofile_RI_locators.Rejected_Reason))
        )
        log = mp_rejected_reason_msg.text
        print(log)
        return log
