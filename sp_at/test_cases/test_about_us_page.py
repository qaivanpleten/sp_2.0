import time

import allure
import pytest

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.about_us_page_elements import AboutPageElements
from sp_at.elements.main_page_elements import MainPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on AboutUs page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#about')

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
@allure.feature('Check elements on AboutUs page')
@allure.story('AboutUs page elements')
def test_aboutus_page(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    about_element = AboutPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#about')
    time.sleep(2)

    general_action.check_element_on_page(about_element.about_title())
    general_action.check_element_on_page(about_element.meet_the_team_title())
    general_action.scroll_page('400')
    general_action.check_element_on_page(about_element.portfolio_block('3'))

    general_action.scroll_page('700')
    general_action.check_element_on_page(about_element.portfolio_block('4'))

    general_action.scroll_page('1200')
    general_action.check_element_on_page(about_element.portfolio_block('5'))

    general_action.scroll_page('1600')
    general_action.check_element_on_page(about_element.portfolio_block('6'))

    general_action.scroll_page('2200')
    general_action.check_element_on_page(about_element.portfolio_block('7'))

    general_action.check_element_on_page(about_element.get_in_touch_button())
    general_action.check_element_on_page(about_element.open_positions_button())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on AboutUs page')
@allure.story('AboutUs page buttons')
def test_buttons(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    about_element = AboutPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#about')
    time.sleep(2)
    general_action.click_on_button(about_element.open_positions_button())
    time.sleep(2)
    general_action.check_url(page_url + '#careers')
