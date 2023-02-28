from selenium.webdriver.common.by import By


class AccountSuccessPage:

    def __init__(self,driver):
        self.driver = driver

    def get_heading(self):
        return self.driver.find_element(By.XPATH,"//div[@id='content']/h1")

    def get_heading_text(self):
        return self.get_heading().text

