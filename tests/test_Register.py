import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.AccountSuccessPage import AccountSuccessPage
from pageobjects.HomePage import HomePage
from pageobjects.RegisterPage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        generated_email = "amotoori"+datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")+"@gmail.com"
        account_success_page = register_page.enter_mandatory_fields_and_click_on_continue_button(
            "Arun","Motoori",generated_email,"1234567890","12345")
        assert account_success_page.get_heading_text().__eq__("Your Account Has Been Created!")

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        generated_email = "amotoori"+datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")+"@gmail.com"
        account_success_page = register_page.enter_all_fields_and_click_on_continue_button(
            "Arun","Motoori",generated_email,"1234567890","12345")
        assert account_success_page.get_heading_text().__eq__("Your Account Has Been Created!")

    def test_register_with_already_registered_account(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.enter_all_fields_and_click_on_continue_button(
            "Arun","Motoori","amotooricap7@gmail.com","1234567890","12345")
        assert register_page.get_warning_message_text().__contains__(
            "Warning: E-Mail Address is already registered!")

    def test_register_without_providing_any_details(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.click_on_continue_button()
        assert register_page.matching_status_of_all_warnings_text("Warning: You must agree to the Privacy Policy!","First Name must be between 1 and 32 characters!","Last Name must be between 1 and 32 characters!","E-Mail Address does not appear to be valid!","Telephone must be between 3 and 32 characters!","Password must be between 4 and 20 characters!")
