import datetime

import pytest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.AccountPage import AccountPage
from pageobjects.HomePage import HomePage
from pageobjects.LoginPage import LoginPage


# Commented by Arun Motoori


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    @pytest.mark.parametrize("email,password",[("amotooricap3@gmail.com", "12345"),("amotooricap5161@gmail.com", "12345"),("amotooricap5@gmail.com","12345")])
    def test_login_with_valid_credentials(self,email,password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_login_page()
        account_page = login_page.enter_credentials_and_login(email,password)
        assert account_page.display_status_of_edit_your_account_information_option()

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_login_page()
        login_page.enter_credentials_and_login("amotooricap4@gmail.com", "1234567890")
        assert login_page.get_warning_message_text().__contains__(
            "Warning: No match for E-Mail Address and/or Password.")

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_login_page()
        generated_invalid_email = "amotoori"+datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")+"@gmail.com"
        login_page.enter_credentials_and_login(generated_invalid_email,"12345")
        assert login_page.get_warning_message_text().__contains__(
            "Warning: No match for E-Mail Address and/or Password.")

    def test_login_with_invalid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_login_page()
        generated_invalid_email = "amotoori"+datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")+"@gmail.com"
        login_page.enter_credentials_and_login(generated_invalid_email,"1234567890")
        assert login_page.get_warning_message_text().__contains__(
            "Warning: No match for E-Mail Address and/or Password.")

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_login_page()
        login_page.click_on_login_button()
        assert login_page.get_warning_message_text().__contains__(
            "Warning: No match for E-Mail Address and/or Password.")

