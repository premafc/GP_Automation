import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Login Page
driver.get("https://gpdev.mygoldenplanet.com/#/")  # Replace with the actual URL

time.sleep(15)

# Use Explicit Wait for the username field
wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds
username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="email"]')))

# Get value entered in the username field
username_value = username_field.get_attribute("value")

# Create a new Excel file and write the username value
wb = Workbook()
ws = wb.active
ws.title = "LoginData"

# Write header and value in the same row
ws.append(["Username", username_value])  # Storing in a single row

# Save the Excel file (using raw string)
excel_path = r"D:\GP_Test_data\Test.xlsx"
wb.save(excel_path)
print(f"Username saved successfully in {excel_path}")

# Close the browser
driver.quit()
