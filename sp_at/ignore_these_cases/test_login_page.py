import time

import allure
import pytest

from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.login_actions import LoginActions
from sp_at.elements.login_page_elements import LoginPageElements
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.elements.users_page_elements import UsersPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check login page features')
@allure.story('Check general elements')
def test_general_elements(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(MainPageElements(fixture_webdriver).url() + '#login')

    # check header elements
    general_action.check_element_on_page(mp_element.logo())
    general_action.check_element_on_page(mp_element.hamburger_menu_button())

    # # check footer elements
    # general_action.check_element_on_page(mp_element.footer_whyus())
    # general_action.check_element_on_page(mp_element.footer_company())
    # general_action.check_element_on_page(mp_element.footer_career())
    # general_action.check_element_on_page(mp_element.footer_faq())
    # general_action.check_element_on_page(mp_element.footer_contact())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check login page features')
@allure.story('Check Login page elements')
def test_page_elements(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    login_element = LoginPageElements(fixture_webdriver)
    general_action.open_page_by_url(MainPageElements(fixture_webdriver).url() + '#login')
    time.sleep(3)

    general_action.check_element_on_page(login_element.login_page_title())
    general_action.check_element_on_page(login_element.login_form())
    general_action.check_element_on_page(login_element.account_id())
    general_action.check_element_on_page(login_element.login_input())
    general_action.check_element_on_page(login_element.login_button())
    general_action.check_element_on_page(login_element.signup_button())
    general_action.check_element_on_page(login_element.use_automatic_button())
    general_action.check_element_on_page(login_element.text_block())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check login page features')
@allure.story('Login canceling')
def test_cancel_login(fixture_webdriver):
    LoginActions(fixture_webdriver).login_cancel('any@email.com')


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check login page features')
@allure.story('Login on the site')
def test_login(fixture_webdriver):
    LoginActions(fixture_webdriver).login_full_case(UsersPageElements(fixture_webdriver).admin_email())
    GeneralActions(fixture_webdriver).check_url(MainPageElements(fixture_webdriver).url() + '#welcome')
