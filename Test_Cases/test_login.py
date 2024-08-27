import pytest
from Test_Locators.homepage import OrangeHRM_Locators
from Utilities.excel_functions import ExcelFunctions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Test_orange:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        excel_file = OrangeHRM_Locators().excel_file
        sheet_number = OrangeHRM_Locators().sheet_number
        self.excel_functions = ExcelFunctions(excel_file, sheet_number)
        yield
        self.driver.close()

    def test_login(self, boot):
        self.driver.get(OrangeHRM_Locators().url)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 8)
        start_row = 2
        end_row = 6

        for row_no in range(start_row, end_row + 1):
            username = self.excel_functions.read_data(row_no, 5)
            password = self.excel_functions.read_data(row_no, 6)
            
            username_element = wait.until(EC.visibility_of_element_located((By.NAME, OrangeHRM_Locators().username)))
            username_element.send_keys(username)
            
            password_element = wait.until(EC.visibility_of_element_located((By.NAME, OrangeHRM_Locators().password)))
            password_element.send_keys(password)
            
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators().submit_button)))
            login_button.click()

            try:
                wait.until(EC.url_matches(OrangeHRM_Locators.dashboard_url))
                self.excel_functions.write_data(row_no, 7, OrangeHRM_Locators.pass_data)
                print("SUCCESS : Logged in with Username")


                profile_image = wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locators().profile_image)))
                profile_image.click()
                logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators().logout_button)))
                logout_button.click()

                wait.until(EC.url_matches(OrangeHRM_Locators.url))
                
            except TimeoutException:
                self.excel_functions.write_data(row_no, 7, OrangeHRM_Locators.fail_data)

                assert self.driver.current_url == OrangeHRM_Locators.url
                print("FAIL : Login failed with Username")

                self.driver.refresh()
