import time

import allure
import pytest

from sp_at.pages.career_page import CareerPage, Body, CareerTextBlock, Button
from sp_at.pages.general_element import Header


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Career page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    CareerPage(fixture_webdriver).open()
    assert Header(fixture_webdriver).present(), "Header is broken. Some element isn't displayed on the page"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Career page')
@allure.story('Career page elements')
def test_career_page(fixture_webdriver):
    CareerPage(fixture_webdriver).open()
    assert Body(fixture_webdriver).present(), "Body is broken. Some element isn't displayed on the page"
    assert CareerTextBlock(fixture_webdriver).present(), "Text area is broken. Some paragraph isn't displayed"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Career page')
@allure.story('Career page buttons')
def test_button(fixture_webdriver):
    CareerPage(fixture_webdriver).open()
    Button(fixture_webdriver).faq().click()
    time.sleep(1)

    assert not CareerPage(fixture_webdriver).check_url(), "The wrong page was opened"
