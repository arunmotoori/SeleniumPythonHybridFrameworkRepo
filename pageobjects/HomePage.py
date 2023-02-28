from selenium.webdriver.common.by import By

from pageobjects.LoginPage import LoginPage
from pageobjects.RegisterPage import RegisterPage
from pageobjects.SearchPage import SearchPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    def get_my_account_option(self):
        return self.driver.find_element(By.XPATH,"//span[text()='My Account']")

    def get_login_option(self):
        return self.driver.find_element(By.LINK_TEXT,"Login")

    def get_register_option(self):
        return self.driver.find_element(By.LINK_TEXT,"Register")

    def get_search_box_field(self):
        return self.driver.find_element(By.NAME,"search")

    def get_search_button(self):
        return self.driver.find_element(By.XPATH,"//div[@id='search']//button")

    def click_on_my_account(self):
        self.get_my_account_option().click()

    def select_login_option(self):
        self.get_login_option().click()
        return LoginPage(self.driver)

    def select_register_option(self):
        self.get_register_option().click()
        return RegisterPage(self.driver)

    def navigate_to_register_page(self):
        self.click_on_my_account()
        return self.select_register_option()

    def enter_product_name_into_search_box_field(self,product_text):
        self.get_search_box_field().send_keys(product_text)

    def click_on_search_button(self):
        self.get_search_button().click()
        return SearchPage(self.driver)

    def enter_product_name_and_click_on_search_button(self,product_text):
        self.enter_product_name_into_search_box_field(product_text)
        return self.click_on_search_button()

    def navigate_login_page(self):
        self.click_on_my_account()
        return self.select_login_option()
