import allure
import pytest

from sp_at.pages.contact_us_page import ContactUsPage, Body, Button
from sp_at.pages.general_element import Header


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Contact page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    ContactUsPage(fixture_webdriver).open()
    assert Header(fixture_webdriver).present(), "Header is broken. Some element isn't displayed on the page"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Contact page')
@allure.story('Contact page elements')
def test_page_element(fixture_webdriver):
    ContactUsPage(fixture_webdriver).open()
    assert Body(fixture_webdriver).present(), "Body is broken. Some element isn't displayed on the page"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Contact page')
@allure.story('FAQ button')
def test_faq_button(fixture_webdriver):
    ContactUsPage(fixture_webdriver).open()
    Button(fixture_webdriver).faq().click()
    assert not ContactUsPage(fixture_webdriver).check_url()


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Contact page')
@allure.story('Try it now button')
def test_try_button(fixture_webdriver):
    ContactUsPage(fixture_webdriver).open()
    Button(fixture_webdriver).try_it_now().click()
    assert not ContactUsPage(fixture_webdriver).check_url()
