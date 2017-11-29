import allure
import pytest

from sp_at.pages.faq_page import FaqPage, Body, Button
from sp_at.pages.general_element import Header


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on FAQ page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    FaqPage(fixture_webdriver).open()
    assert Header(fixture_webdriver).present(), "Header is broken. Some element isn't displayed on the page"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on FAQ page')
@allure.story('FAQ page elements')
def test_page_element(fixture_webdriver):
    FaqPage(fixture_webdriver).open()
    assert Body(fixture_webdriver).present(), "Body is broken. Some element isn't displayed on the page"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on FAQ page')
@allure.story('FAQ page button')
def test_buttons(fixture_webdriver):
    FaqPage(fixture_webdriver).open()
    Button(fixture_webdriver).try_it_now().click()
    assert not FaqPage(fixture_webdriver).check_url()
