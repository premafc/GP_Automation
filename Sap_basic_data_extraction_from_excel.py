import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
from openpyxl.styles import Font

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the Login Page
driver.get("https://salesdemo.successfactors.eu/sf/start/#/companyEntry")

try:
    # Wait for the Company id field and enter the Company ID
    company_id_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Company ID"]'))
    )
    company_id_field.send_keys("SFCPART000496")

    # Wait for the Continue button and click it
    continue_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="continueToLoginBtn-BDI-content"]'))
    )
    continue_button.click()

    time.sleep(10)

    # Wait for the Username field and enter the username
    username_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="j_username"]'))
    )
    username_field.send_keys("sfadmin")

    # Wait for the Password field and enter the password
    password_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Password"]'))
    )
    password_field.send_keys("Bpt@2025")

    # Wait for the Login button and click it
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="fn-button__text"]'))
    )
    login_button.click()

    print("Login successful!")

    time.sleep(10)

    # Wait for the View my profile button and click it
    View_my_profile_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text() = 'View My Profile']"))
    )
    View_my_profile_button.click()
    time.sleep(15)

    print("Navigated to Profile page successfully!")

    # Use Explicit Wait for the username field
    wait = WebDriverWait(driver, 30)  # Wait up to 20 seconds
    Salutation_field = wait.until(EC.presence_of_element_located((By.XPATH, '(//*[@class="Text_text_b95k2_1 PreviousValue_currentValue__dmxiM"])[1]')))
    First_Name_field = wait.until(EC.presence_of_element_located((By.XPATH, '(//*[@class="Text_text_b95k2_1 PreviousValue_currentValue__dmxiM"])[2]')))
    Last_Name_field = wait.until(EC.presence_of_element_located((By.XPATH, '(//*[@class="Text_text_b95k2_1 PreviousValue_currentValue__dmxiM"])[3]')))
    Preferred_Name_field = wait.until(EC.presence_of_element_located((By.XPATH, '(//*[@class="Text_text_b95k2_1 PreviousValue_currentValue__dmxiM"])[4]')))
    Gender_field = wait.until(EC.presence_of_element_located((By.XPATH, '(//*[@class="Text_text_b95k2_1 PreviousValue_currentValue__dmxiM"])[5]')))

    # Get value entered in the username field

    #Salutation_value = Salutation_field.get_attribute("value")
    #First_Name_value = First_Name_field.get_attribute("value")

    Salutation_value = Salutation_field.text
    First_Name_value = First_Name_field.text
    Last_Name_value = Last_Name_field.text
    Preferred_Name_value = Preferred_Name_field.text
    Gender_value = Gender_field.text

    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(2)  # Small delay to allow UI updates

    # Create a new Excel file and write the username value
    wb = Workbook()
    ws = wb.active
    ws.title = "ProfileData"

    # Insert heading row
    ws.append(["Personal Information"])  # Heading
    heading_cell = ws["A1"]
    heading_cell.font = Font(bold=True, size=12)
    ws.append([])  # Empty row for spacing

    # Write header and value in the same row
    ws.append(["Salutation", Salutation_value])  # Storing in a single row
    ws.append(["Firstname",First_Name_value])
    ws.append(["Lastname", Last_Name_value])
    ws.append(["Preferred name", Preferred_Name_value])
    ws.append(["Gender", Gender_value])

    # Save the Excel file (using raw string)
    excel_path = r"D:\GP_Test_data\Test.xlsx"
    wb.save(excel_path)
    print(f"Values saved successfully in {excel_path}")

    time.sleep(15)

except Exception as e:
    print(f"Error occurred: {e}")
