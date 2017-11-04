import allure
import pytest

from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.login_actions import LoginActions
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.elements.users_page_elements import UsersPageElements
from sp_at.elements.welcome_page_elements import WelcomePageElements

@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check Welcome page features')
@allure.story('Check general elements')
def test_page_elements(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    welcome_elements = WelcomePageElements(fixture_webdriver)
    LoginActions(fixture_webdriver).login_full_case(UsersPageElements(fixture_webdriver).admin_email())

    # check elements
    general_action.check_element_on_page(mp_element.logo())
    general_action.check_element_on_page(mp_element.hamburger_menu_button())

    general_action.check_element_on_page(welcome_elements.logout_button())
    general_action.check_element_on_page(welcome_elements.welcome_time())
    general_action.check_element_on_page(welcome_elements.content_block())
    general_action.check_element_on_page(welcome_elements.dashboard_button())
    general_action.check_element_on_page(welcome_elements.partner_button())

    # # check footer elements
    # general_action.check_element_on_page(mp_element.footer_whyus())
    # general_action.check_element_on_page(mp_element.footer_company())
    # general_action.check_element_on_page(mp_element.footer_career())
    # general_action.check_element_on_page(mp_element.footer_faq())
    # general_action.check_element_on_page(mp_element.footer_contact())
