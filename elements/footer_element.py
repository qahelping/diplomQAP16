import allure

from helpers.base_page import BasePage


class FooterElement(BasePage):
    LANG = '//*[@value="{lang}"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Assert lan is visible")
    def assert_lang_visible(self):
        self.wait_for(self.LANG.format(lang='en'))
        self.wait_for(self.LANG.format(lang='ja'))
        self.wait_for(self.LANG.format(lang='es'))
        self.wait_for(self.LANG.format(lang='de'))
