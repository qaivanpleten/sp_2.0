import time

import allure
import pytest

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.elements.why_page_elements import WhyPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on WhyUs page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#why')

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
@allure.feature('Check elements on WhyUs page')
@allure.story('WhyUs page elements')
def test_page_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    why_element = WhyPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#why')
    time.sleep(3)

    general_action.check_element_on_page(why_element.why_title())
    general_action.check_element_on_page(why_element.ten_reasons_title())
    general_action.check_element_on_page(why_element.ten_reasons_text_block())
    general_action.scroll_page('1000')
    general_action.check_element_on_page(why_element.have_question_button())
    general_action.check_element_on_page(why_element.try_it_button())
