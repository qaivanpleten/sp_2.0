import time

import allure
import pytest

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.install_page_elements import InstallPageElements
from sp_at.elements.main_page_elements import MainPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Install page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#install')

    # check header elements
    general_action.check_element_on_page(mp_element.logo())
    general_action.check_element_on_page(mp_element.signup_button())
    general_action.check_element_on_page(mp_element.login_button())
    general_action.check_element_on_page(mp_element.hamburger_menu_button())

    # check footer elements
    # general_action.check_element_on_page(mp_element.footer_whyus())
    # general_action.check_element_on_page(mp_element.footer_company())
    # general_action.check_element_on_page(mp_element.footer_career())
    # general_action.check_element_on_page(mp_element.footer_faq())
    # general_action.check_element_on_page(mp_element.footer_contact())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Install page')
@allure.story('Install page elements')
def test_page_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    install_element = InstallPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#install')
    time.sleep(3)

    general_action.check_element_on_page(install_element.install_title())
    general_action.check_element_on_page(install_element.install_on_ios())
    general_action.check_element_on_page(install_element.install_desktop())
    general_action.check_element_on_page(install_element.install_on_android())
    general_action.scroll_page('500')
    general_action.check_element_on_page(install_element.content_block())
    general_action.check_element_on_page(install_element.troubleshooting_title())
    general_action.check_element_on_page(install_element.troubleshooting_block())

    general_action.click_on_button(install_element.troubleshooting_button_how_do_())
    general_action.check_element_on_page(install_element.troubleshooting_text_how_do_())

    general_action.scroll_page('1100')
    time.sleep(2)
    general_action.click_on_button(install_element.troubleshooting_button_app_is())
    general_action.check_element_on_page(install_element.troubleshooting_text_how_do_())

    general_action.scroll_page('1400')
    time.sleep(2)
    general_action.click_on_button(install_element.troubleshooting_button_download())
    general_action.check_element_on_page(install_element.troubleshooting_text_download())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Install page')
@allure.story('Install page button')
def test_ios_button(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    install_element = InstallPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#install')
    time.sleep(3)

    general_action.click_on_button(install_element.install_on_ios())
    general_action.check_url('https://beta.itunes.apple.com/v1/app/1140636912')
