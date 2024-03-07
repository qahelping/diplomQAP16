import allure

from helpers.base_page import BasePage
from pages.locators import SearchLocators


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_locators = SearchLocators()

    @allure.step("Assert info block is visible")
    def assert_that_info_block_is_visible(self):
        assert self.wait_for(self.main_locators.CALLOUT_BLOCK)
