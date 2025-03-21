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
    wait = WebDriverWait(driver, 30)

    # Wait for the Company ID field and enter the ID
    company_id_field = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Enter Company ID"]'))
    )
    company_id_field.send_keys("SFCPART000496")

    # Click Continue
    continue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="continueToLoginBtn-BDI-content"]'))
    )
    continue_button.click()

    time.sleep(10)

    # Enter Username
    username_field = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="j_username"]'))
    )
    username_field.send_keys("sfadmin")

    # Enter Password
    password_field = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@placeholder="Password"]'))
    )
    password_field.send_keys("Bpt@2025")

    # Click Login
    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="fn-button__text"]'))
    )
    login_button.click()

    print("Login successful!")
    time.sleep(10)

    # Navigate to Profile Page
    profile_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[text() = 'View My Profile']"))
    )
    profile_button.click()

    time.sleep(15)
    print("Navigated to Profile page successfully!")

    # Define field names and corresponding XPaths
    fields = {
        "Salutation": '(//*[@class="Text_text_b95k2_1 PreviousValue_currentValue__dmxiM"])[1]',
        "Firstname": '(//*[@class="Text_text_b95k2_1 PreviousValue_currentValue__dmxiM"])[2]',
        "Lastname": '(//*[@class="Text_text_b95k2_1 PreviousValue_currentValue__dmxiM"])[3]',
        "Preferred name": '(//*[@class="Text_text_b95k2_1 PreviousValue_currentValue__dmxiM"])[4]',
        "Gender": '(//*[@class="Text_text_b95k2_1 PreviousValue_currentValue__dmxiM"])[5]'
    }

    # Scroll to update UI if necessary
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

    # Store extracted values
    extracted_values = {}

    for key, xpath in fields.items():
        field_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        extracted_values[key] = field_element.text

    # Create a new Excel file and write data
    wb = Workbook()
    ws = wb.active
    ws.title = "ProfileData"

    # Insert heading
    ws.append(["Personal Information"])
    heading_cell = ws["A1"]
    heading_cell.font = Font(bold=True, size=12)
    ws.append([])  # Empty row for spacing

    # Write extracted values to Excel
    for key, value in extracted_values.items():
        ws.append([key, value])

    # Save the Excel file
    excel_path = r"D:\GP_Test_data\Test.xlsx"
    wb.save(excel_path)
    print(f"Values saved successfully in {excel_path}")

    time.sleep(15)

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    driver.quit()
