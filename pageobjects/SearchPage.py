from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self,driver):
        self.driver = driver

    def get_hp_product(self):
        return self.driver.find_element(By.LINK_TEXT,"HP LP3065")

    def get_message(self):
        return self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p")

    def get_display_status_of_product(self):
        return self.get_hp_product().is_displayed()

    def get_message_text(self):
        return self.get_message().text

