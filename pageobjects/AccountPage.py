from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    def get_edit_your_account_information_option(self):
        return self.driver.find_element(By.LINK_TEXT,"Edit your account information")

    def display_status_of_edit_your_account_information_option(self):
        return self.get_edit_your_account_information_option().is_displayed()

