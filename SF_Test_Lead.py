from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


class Lead:

    def login_lead_creation(self):
        try:
            # Set up ChromeDriver service and initialize WebDriver
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            driver.maximize_window()
            driver.get("https://energy-data-4161--clientface.sandbox.my.salesforce.com/")
            time.sleep(5)  # Allow time for the page to load

            # Login page Username Field:
            username_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
            )
            username_field.send_keys("jeffrin@corewireindia.com.clientface")

            # Login page password field:
            password_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
            )
            password_field.send_keys("Info@1234")

            # Login button:
            login_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@name="Login"]'))
            )
            login_button.click()
            print("User Login Successfully.")
            time.sleep(20)
            #"""
            # New Lead button:
            lead_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@title,'New')]"))
            )
            lead_button.click()
            time.sleep(3)

            # dropdown click button:
            dropdown_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@name='salutation' and @role='combobox']"))
            )
            dropdown_button.click()
            time.sleep(2)

            # dropdown MR. click button:
            lead_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@title="Mr."]'))
            )
            lead_button.click()

            # Lead page Last name field:
            lastname_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Last Name"]'))
            )
            lastname_field.send_keys("WiproTest")
            time.sleep(1)

            # Find the modal container
            modal_container = driver.find_element(By.CLASS_NAME, "actionBody")

            # Scroll down by 250 pixels (between 200 and 300)
            driver.execute_script("arguments[0].scrollBy(0, 250);", modal_container)

            time.sleep(2)  # Small delay to observe the scroll

            # Lead page company name field:
            company_name_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@name="Company"]'))
            )
            company_name_field.send_keys("Wipro")
            time.sleep(1)

            # Enquire Date picker click :
            enquire_Date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@title,'Select a date for Enquiry Date')]//lightning-primitive-icon[contains(@exportparts,'icon')]"))
            )
            enquire_Date.click()
            time.sleep(2)

            # Today Date click :
            today_Date = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH,"//button[@name='today']"))
            )
            today_Date.click()
            time.sleep(2)

            # Lead page company name field:
            email_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@inputmode="email"]'))
            )
            email_field.send_keys("prem@yopmail.com")
            time.sleep(1)

            # Scroll down by 250 pixels (between 200 and 300)
            driver.execute_script("arguments[0].scrollBy(0, 150);", modal_container)
            time.sleep(1)

            # Lead page company name field:
            mobile_number_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@name="MobilePhone"]'))
            )
            mobile_number_field.send_keys("8870394165")
            time.sleep(1)

            # save button:
            save_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@name="SaveEdit"]'))
            )
            save_button.click()
            time.sleep(10)
            print("Lead Created Successfully.")

            # convert button:
            time.sleep(1)
            convert_button = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Converted']"))
            )
            driver.execute_script("arguments[0].click();", convert_button)
            time.sleep(5)
            # '(//*[@data-name="converted"])[2]'

            # convert status button:
            convert_status_button = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="uiOutputText"]'))
            )
            driver.execute_script("arguments[0].click();", convert_status_button)
            time.sleep(3)

            # convert Lead button:
            convert_lead_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Convert']"))
            )
            convert_lead_button.click()
            print("Your Lead has been Converted.")
            time.sleep(5)

            # Go to Leads button:
            go_to_leads_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@class="slds-button slds-button_brand"]'))
            )
            go_to_leads_button.click()
            time.sleep(5)
            #"""
            # Click Accounts module:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//a[@title='Accounts']"))
            )
            driver.execute_script("arguments[0].click();", element)
            time.sleep(3)

            # "//a[contains(@title,'Accounts')]"
            # Accounts page search name field:

            search_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@name="Account-search-input"]'))
            )
            search_field.send_keys("Wipro")
            # Press Enter key
            search_field.send_keys(Keys.ENTER)
            time.sleep(3)

            # Account Link Open Button :
            account_link_open = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@title="Wipro"]'))
            )
            account_link_open.click()
            time.sleep(3)

            # oppourtunity Link Open Button :
            oppourtunity_link_open = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Wipro-']"))
            )
            oppourtunity_link_open.click()
            time.sleep(5)

            # Add_product_button :
            Add_product_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '(//*[@title="Add Products"])[1]'))
            )
            Add_product_button.click()

            """
            # save button:
            product_save_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '(//*[@class=" label bBody"])[4]'))
            )
            product_save_button.click()
            time.sleep(5)


            # add_product_check_box:
            add_product_check_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "(//span[contains(@class, 'slds-checkbox_faux')])[3]"))
            )
            add_product_check_box.click()
            

            add_product_check_box = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[4]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/span[1]/div[1]/span[1]"))
            )
            #driver.execute_script("arguments[3].scrollIntoView();", add_product_check_box)
            add_product_check_box.click()
            
            search_product_field = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Search Products..."]'))
            )
            search_product_field.send_keys("100")
            time.sleep(5)

            product_choose = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '(//*[@title="100"])[1]'))
            )
            product_choose.click()
           
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@class="modal-container slds-modal__container"]'))
                # Update popup locator if needed
            )

            iframe = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@class="modal-container slds-modal__container"]'))  # Adjust if needed
            )
            driver.switch_to.frame(iframe)
             """
            search_product_field = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@placeholder="Search Products..."]'))
            )
            search_product_field.send_keys(Keys.TAB)
            time.sleep(2)
            search_product_field.send_keys(Keys.TAB)
            time.sleep(2)
            search_product_field.send_keys(Keys.ENTER)
            time.sleep(2)

            product_checkbox_button = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '(//*[@class="slds-checkbox--faux slds-checkbox_faux"])[2]'))
            )
            product_checkbox_button.click()
            time.sleep(3)
            """
            for _ in range(132):
                search_product_field.send_keys(Keys.TAB)

            # Next button:
            product_next_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '(//*[@class=" label bBody"])[4]'))
            )
            product_next_button.click()
            time.sleep(10)
            """
            """
            # Lead button:
            lead_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '(//*[@part="icon"])[9]'))
            )
            lead_button.click()
            time.sleep(5)
                
            lead_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//div[1]//one-appnav[1]//div[1]//one-app-nav-bar[1]//nav[1]//div[1]//one-app-nav-bar-item-root[1]//one-app-nav-bar-item-dropdown[1]//div[1]//one-app-nav-bar-menu-button[1]//div[1]//div[1]//slot[1]//one-app-nav-bar-menu-item[1]//a[1]//span[1]//lightning-icon[1]//span[1]//lightning-primitive-icon[1]//*[name()='svg']"))
            )
            # EC.element_to_be_clickable((By.XPATH, "//div[1]//one-appnav[1]//div[1]//one-app-nav-bar[1]//nav[1]//div[1]//one-app-nav-bar-item-root[1]//one-app-nav-bar-item-dropdown[1]//div[1]//one-app-nav-bar-menu-button[1]//div[1]//div[1]//slot[1]//one-app-nav-bar-menu-item[1]//a[1]//span[1]//lightning-icon[1]//span[1]//lightning-primitive-icon[1]//*[name()='svg']"))
            lead_button.click()
            time.sleep(10)
            """

            return driver  # Return driver instance for further use

        except Exception as e:
            print("Login_Error:", e)
            return None  # Return None in case of failure

# Example usage:
lead = Lead()
driver_instance = lead.login_lead_creation()

if driver_instance:
    print("Proceeding with further actions...")
else:
    print("script failed. Exiting test.")
