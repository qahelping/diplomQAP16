import allure

from data import DOMEN
from elements.footer_element import FooterElement


@allure.title("3. Footer: lang")
def test_footer_lang(driver):
    footer_element = FooterElement(driver)
    footer_element.open(DOMEN)

    footer_element.assert_lang_visible()