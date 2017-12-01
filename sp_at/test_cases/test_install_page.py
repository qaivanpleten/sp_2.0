import allure
import pytest

from sp_at.pages.general_element import Header
from sp_at.pages.install_page import InstallPage, Body


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Install page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    InstallPage(fixture_webdriver).open()
    assert InstallPage(fixture_webdriver).check_sonicpass_url(), "The wrong page was opened, or the URL is incorrect"
    assert Header(fixture_webdriver).present(), "Header is broken. Some element isn't displayed on the page"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Install page')
@allure.story('Install page elements')
def test_page_elements(fixture_webdriver):
    InstallPage(fixture_webdriver).open()
    assert Body(fixture_webdriver).present(), "Body is broken. Some element isn't displayed on the page"



