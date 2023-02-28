import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobjects.HomePage import HomePage
from pageobjects.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.enter_product_name_and_click_on_search_button("HP")
        assert search_page.get_display_status_of_product()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.enter_product_name_and_click_on_search_button("Honda")
        assert search_page.get_message_text().__eq__(
            "There is no product that matches the search criteria.")

    def test_search_without_any_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.click_on_search_button()
        assert search_page.get_message_text().__eq__(
            "There is no product that matches the search criteria.")

