import pytest
import time
from Pages.Forgotusername import Forgotusername

@pytest.mark.usefixtures("setup_class")
class Testforgotusername:
    driver = None  # Explicitly define the driver attribute
    url = "https://gold.groupnpay.com/#/"
    
    def test_01_forgot_username(self):
        time.sleep(2)
        self.driver.get(self.url)
        obj_Forgotusername = Forgotusername(self.driver)
        obj_Forgotusername.forgot_user_name(self.driver)
    