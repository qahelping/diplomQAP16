import allure

from pages import MainPage
from pages.search_page import SearchPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@allure.title("1. Open search page")
def test_open_search_page(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.click_on_search()

    search_page = SearchPage(driver)
    search_page.assert_that_info_block_is_visible()


@allure.title("2. Search")
@pytest.mark.parametrize("input,expected", [
    ('pytest', 'pytest: simple powerful testing with Python'),
    ('        ', 'validate input of openwhisk'),
    ('', 'validate input of openwhisk'),
    ('selenium webdriver', 'selenium-webdriver-extender'),
    ('s@#$%^&', '0 проектов по запросу «@#$%^&»'),
])
def test_search(driver, input, expected):
    main_page = MainPage(driver)
    main_page.open_page()
    main_page.search_text(input)

    main_page.assert_text(expected)



