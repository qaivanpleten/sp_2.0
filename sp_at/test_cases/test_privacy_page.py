import time

import allure
import pytest

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.elements.privacy_page_elemnts import PrivacyPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Privacy page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#privacy')

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
@allure.feature('Check elements on Privacy page')
@allure.story('Privacy page elements')
def test_page_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    privacy_element = PrivacyPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#privacy')
    time.sleep(3)

    general_action.check_element_on_page(privacy_element.privacy_title())
    general_action.check_element_on_page(privacy_element.first_paragraph())
    general_action.check_element_on_page(privacy_element.second_paragraph())
    general_action.scroll_page('500')
    general_action.check_element_on_page(privacy_element.third_paragraph())
    general_action.check_element_on_page(privacy_element.fourth_paragraph())
    general_action.scroll_page('800')
    general_action.check_element_on_page(privacy_element.fifth_paragraph())
    general_action.scroll_page('1500')
    general_action.check_element_on_page(privacy_element.sixth_paragraph())
    general_action.check_element_on_page(privacy_element.seventh_paragraph())
    general_action.check_element_on_page(privacy_element.eighth_paragraph())
    general_action.check_element_on_page(privacy_element.questions_button())
