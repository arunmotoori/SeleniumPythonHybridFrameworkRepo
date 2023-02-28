from selenium.webdriver.common.by import By

from pageobjects.AccountSuccessPage import AccountSuccessPage


class RegisterPage:

    def __init__(self,driver):
        self.driver = driver

    def get_first_name_field(self):
        return self.driver.find_element(By.ID,"input-firstname")

    def get_last_name_field(self):
        return self.driver.find_element(By.ID,"input-lastname")

    def get_email_field(self):
        return self.driver.find_element(By.ID,"input-email")

    def get_telephone_field(self):
        return self.driver.find_element(By.ID,"input-telephone")

    def get_password_field(self):
        return self.driver.find_element(By.ID,"input-password")

    def get_password_confirm_field(self):
        return self.driver.find_element(By.ID,"input-confirm")

    def get_yes_newsletter_option(self):
        return self.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']")

    def get_privacy_policy_field(self):
        return self.driver.find_element(By.NAME,"agree")

    def get_continue_button(self):
        return self.driver.find_element(By.XPATH,"//input[@value='Continue']")

    def get_warning_message(self):
        return self.driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]")

    def get_privacy_policy_warning(self):
        return self.driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]")

    def get_first_name_warning(self):
        return self.driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div")

    def get_last_name_warning(self):
        return self.driver.find_element(By.XPATH,"//input[@id='input-lastname']/following-sibling::div")

    def get_email_warning(self):
        return self.driver.find_element(By.XPATH,"//input[@id='input-email']/following-sibling::div")

    def get_telephone_warning(self):
        return self.driver.find_element(By.XPATH,"//input[@id='input-telephone']/following-sibling::div")

    def get_password_warning(self):
        return self.driver.find_element(By.XPATH,"//input[@id='input-password']/following-sibling::div")

    def enter_first_name(self,first_name_text):
        self.get_first_name_field().send_keys(first_name_text)

    def enter_last_name(self,last_name_text):
        self.get_last_name_field().send_keys(last_name_text)

    def enter_email(self,email_text):
        self.get_email_field().send_keys(email_text)

    def enter_telephone_number(self,telephone_text):
        self.get_telephone_field().send_keys(telephone_text)

    def enter_password(self,password_text):
        self.get_password_field().send_keys(password_text)

    def enter_password_confirm(self,password_text):
        self.get_password_confirm_field().send_keys(password_text)

    def select_privacy_policy(self):
        self.get_privacy_policy_field().click()

    def click_on_continue_button(self):
        self.get_continue_button().click()
        return AccountSuccessPage(self.driver)

    def enter_mandatory_fields_and_click_on_continue_button(self,first_name_text,last_name_text,email_text,telephone_text,password_text):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone_number(telephone_text)
        self.enter_password(password_text)
        self.enter_password_confirm(password_text)
        self.select_privacy_policy()
        return self.click_on_continue_button()

    def enter_all_fields_and_click_on_continue_button(self,first_name_text,last_name_text,email_text,telephone_text,password_text):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone_number(telephone_text)
        self.enter_password(password_text)
        self.enter_password_confirm(password_text)
        self.select_yes_newsletter_option()
        self.select_privacy_policy()
        return self.click_on_continue_button()

    def select_yes_newsletter_option(self):
        self.get_yes_newsletter_option().click()

    def get_warning_message_text(self):
        return self.get_warning_message().text

    def get_privacy_policy_warning_text(self):
        return self.get_privacy_policy_warning().text

    def get_first_name_warning_text(self):
        return self.get_first_name_warning().text

    def get_last_name_warning_text(self):
        return self.get_last_name_warning().text

    def get_email_warning_text(self):
        return self.get_email_warning().text

    def get_telephone_warning_text(self):
        return self.get_telephone_warning().text

    def get_password_warning_text(self):
        return self.get_password_warning().text

    def matching_status_of_all_warnings_text(self,expected_privacy_policy_warning_text,expected_first_name_warning_text,
                                             expected_last_name_warning_text,expected_email_warning_text,
                                             expected_telephone_warning_text,expected_password_warning_text):
        privacy_policy_warning_text = self.get_privacy_policy_warning_text()
        first_name_warning_text = self.get_first_name_warning_text()
        last_name_warning_text = self.get_last_name_warning_text()
        email_warning_text = self.get_email_warning_text()
        telephone_warning_text = self.get_telephone_warning_text()
        password_warning_text = self.get_password_warning_text()

        result1 = privacy_policy_warning_text.__contains__(expected_privacy_policy_warning_text)
        result2 = first_name_warning_text.__contains__(expected_first_name_warning_text)
        result3 = last_name_warning_text.__contains__(expected_last_name_warning_text)
        result4 = email_warning_text.__contains__(expected_email_warning_text)
        result5 = telephone_warning_text.__contains__(expected_telephone_warning_text)
        result6 = password_warning_text.__contains__(expected_password_warning_text)

        if result1 and result2 and result3 and result4 and result5 and result6:
            return True
        else:
            return False





