import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session", autouse=False)
def driver():
    web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    web_driver.implicitly_wait(5)
    web_driver.minimize_window()

    yield web_driver

    web_driver.quit()
