import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook


# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the Login Page
driver.get("https://gpdev.mygoldenplanet.com/#/")  # Replace with the actual URL

try:
    # Wait for the Username field and enter the username
    username_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="email"]'))
    )
    username_field.send_keys("prem27@yopmail.com")

    # Wait for the Password field and enter the password
    password_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
    )
    password_field.send_keys("prem@123")

    # Wait for the Login button and click it
    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="login_btn"]'))
    )
    login_button.click()

    print("Login successful!")

    time.sleep(10)

    # Wait for the User Profile icon and click it
    user_profile_icon = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '(//*[@class="profile_icon"])[2]'))
    )
    user_profile_icon.click()

    time.sleep(3)  # Wait to observe the action

    # Wait for the "My Profile" menu item and click it
    myprofile_icon = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text() = 'My Profile']"))
    )
    myprofile_icon.click()

    print("Navigated to My Profile page successfully!")
    time.sleep(5)

    # Use Explicit Wait for the username field
    wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds
    Name_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')))

    # Get value entered in the username field
    Name_value = Name_field.get_attribute("value")

    # Create a new Excel file and write the username value
    wb = Workbook()
    ws = wb.active
    ws.title = "LoginData"

    # Write header and value in the same row
    ws.append(["Username", Name_value])  # Storing in a single row

    # Save the Excel file (using raw string)
    excel_path = r"D:\GP_Test_data\Test.xlsx"
    wb.save(excel_path)
    print(f"Username saved successfully in {excel_path}")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Close the browser after execution
    time.sleep(5)  # Wait to observe the result
    driver.quit()
