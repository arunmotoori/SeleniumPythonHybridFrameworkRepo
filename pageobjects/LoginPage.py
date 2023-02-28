from selenium.webdriver.common.by import By

from pageobjects.AccountPage import AccountPage


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def get_email_field(self):
        return self.driver.find_element(By.ID,"input-email")

    def get_password_field(self):
        return self.driver.find_element(By.ID,"input-password")

    def get_login_button(self):
        return self.driver.find_element(By.XPATH,"//input[@value='Login']")

    def get_warning_message_element(self):
        return self.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]")

    def enter_email_address(self,email_text):
        self.get_email_field().send_keys(email_text)

    def enter_password(self,password_text):
        self.get_password_field().send_keys(password_text)

    def click_on_login_button(self):
        self.get_login_button().click()
        return AccountPage(self.driver)

    def get_warning_message_text(self):
        return self.get_warning_message_element().text

    def enter_credentials_and_login(self,email_text,password_text):
        self.enter_email_address(email_text)
        self.enter_password(password_text)
        return self.click_on_login_button()


