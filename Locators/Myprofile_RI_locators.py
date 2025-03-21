# MY Profile Page XPaths [MY_PROFILE_RESIDENT_INDIAN]

Role_RI = "//*[text () = 'RESIDENT INDIAN']"
Role_NRI = "//*[text() = 'NON-RESIDENT INDIAN']"

# Terms for offer document : X paths:

MP_Terms_and_Offer = '//*[@class="login_label temscheckbox_div"] //*[@type="checkbox"]'
X_Mark_Terms_and_offer = 'svg.moda_closel_icon'
MP_Alert_Yes = '//*[@class="modal_btn"]'
MP_Alert_No = '//*[@class="modal_btn error"]'
MP_Submit1 = '//*[@id="modalsubmitoffer"]'
Success = "//*[text() ='OK']"

Terms_for_offer_error_message = "//*[text() ='Please agree the Terms for the Offer']"
Terms_for_offer_pop_up_message = "//*[text() ='Thanks for Accepting the terms for the Offer.']"


NameofApplicant = '//input[@placeholder="First Name"]'
User_category = '.css-1xc3v61-indicatorContainer'
Minor = "//*[text()='MINOR']"
Major = "//*[text() ='MAJOR']"

Status_of_Applicant = '.css-1xc3v61-indicatorContainer'
Individual = "//*[text()='INDIVIDUAL']"
HUF = "//*[text() = 'HUF']"
Body_Corporate = "//div[text()='BODY CORPORATE']"
Trust = "//div[text()='TRUST']"

Date_of_Birth = '//*[@class="react-datepicker__input-container react-datepicker__view-calendar-icon"]'
Date_month = "//*[text() = '1']"

PanNumber = '//*[@id="panNo"]'
Aadhaar_Number = '//*[@id="aadhaar"]'
PermanentAddress = '// input[ @ placeholder = "Permanent Address"]'


Country = '.css-1xc3v61-indicatorContainer'
India1 = "//*[text() = 'INDIA']"
USA1 = "(//*[text()='USA'])[1]"
state = '.css-1xc3v61-indicatorContainer'
State1 = "//*[text() ='Andhra Pradesh']"
City1 = '// input[ @ name = "city1"]'
PostalCode1 = '// input[ @ id = "pincode1"]'

Address_for_correspondence = '// input[ @ placeholder = "Address for correspondence"]'
City2 = '// input[ @ id = "city2"]'
State2 = '// input[ @ id = "state2"]'
India2 = "(//*[text()='INDIA'])[2]"
USA2 = "(//*[text()='USA'])[2]"
PostalCode2 = '// input[ @ id = "pincode2"]'

Same_as_permanentAddress = '//*[@id="agreeCheckbox"]'

UploadPan = '//input[@id="uploadPan"]'
UploadAddressProof = '//*[@id="aadhaarImg"]'  # //input[@id="aadhaarImg"]
UploadProfilePhoto = '//*[@id="profileImg"]'  # //input[@id="profileImg"]
Terms_and_conditions = '//input[@id="iagree"]'
Save_as_draft = '//*[@id="saveussubmit"]'
MP_Submit2 = '//button[@type="submit"]'
MP_Confirmation_Yes = '//*[@class="modal_btn"]'
MP_Confirmation_No = '//*[@class="modal_btn error"]'
MP_Confimation_X_Mark = '//*[@class="modal_close_icon"]'
Ok_button = "//*[text() ='OK']"

Draft_popup_message = "//*[text() ='Your application has been saved as draft.']"

# Minor:

Guardian_name = '//*[@id="guardianName"]'
Guardian_date_of_birth = '(//*[@class="react-datepicker__input-container react-datepicker__view-calendar-icon"])[2]'
Guardian_relation = '//*[@id="guardianRelation"]'
Guardian_pan = '//*[@id="guardianPan"]'
Guardian_aadhar = '//*[@id="guardianAadhaar"]'
Upload_guardian_pan = '//*[@id="guardianPanImg"]'
Upload_guardian_aadhar = '//*[@id="guardianAadhaarImg"]'

my_profile_icon = '(//*[@class="profile_icon"])[2]'
my_profile = "//*[text() = 'My Profile']"
Rejected_Reason = "//*[text() = 'User KYC Rejected Successfully.']"

submit_pop_up_msg = "The above information provided has been updated.\n" \
                    "The files uploaded have been received.\n" \
                    "KYC verification is being processed.\n"

