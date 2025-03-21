import pytest
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""
@pytest.fixture(scope="session")  # Scope is session to keep browser open throughout
def setup_browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://gpdev.mygoldenplanet.com/#/")
    time.sleep(5)  # Let the page load
    yield driver  # Return driver to tests
    driver.quit()  # Close after all tests
"""

@pytest.fixture(scope="class")
def setup_class(request):
    # Set up ChromeDriver service and initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://gpdev.mygoldenplanet.com/#/")
    time.sleep(5)  # Allow time for the page to load

    # Debugging: Print the driver object to confirm it's being initialized correctly
    print(f"Driver initialized: {driver}")

    # Provide the driver instance to the test class
    request.cls.driver = driver

    yield  # Execute test methods

    driver.quit()  # Teardown





