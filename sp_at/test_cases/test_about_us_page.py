import time

import allure
import pytest

from sp_at.pages.about_us_page import AboutUsPage, Button, Body, MeetTheTeamBlock
from sp_at.pages.general_element import Header


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on AboutUs page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    AboutUsPage(fixture_webdriver).open()
    assert Header(fixture_webdriver).present(), "Header is broken"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on AboutUs page')
@allure.story('AboutUs page elements')
def test_aboutus_page(fixture_webdriver):
    AboutUsPage(fixture_webdriver).open()
    assert Body(fixture_webdriver).present(), "Body is broken, some of the element is missed"
    assert MeetTheTeamBlock(fixture_webdriver).present(), "Meet hte team block is broken"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on AboutUs page')
@allure.story('AboutUs page buttons')
def test_buttons(fixture_webdriver):
    AboutUsPage(fixture_webdriver).open()
    Button(fixture_webdriver).open_positions().click()
    time.sleep(1)

    assert not AboutUsPage(fixture_webdriver).check_url(), "The wrong page was opened"
