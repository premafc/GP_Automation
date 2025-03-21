import pytest

# Define the test file and Allure reports directory
test_file = "smoke_test_file.py"  # Adjust the path to your smoke test file
allure_report_dir = "D:/Automation/GP_Automation/Reports"

# Run pytest with Allure report generation
pytest_args = [
    test_file,
    "-v",  # Verbose mode
    "-s",  # Disable output capture
    f"--alluredir={allure_report_dir}"  # Allure report directory
]

# Run pytest programmatically
pytest.main(pytest_args)
