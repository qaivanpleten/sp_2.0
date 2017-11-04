import allure
import pytest

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.faq_page_elements import FaqPageElements
from sp_at.elements.main_page_elements import MainPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on FAQ page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#faq')

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
@allure.feature('Check elements on FAQ page')
@allure.story('FAQ page elements')
def test_page_element(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    f_element = FaqPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#faq')

    general_action.check_element_on_page(f_element.faq_page_title())
    general_action.check_element_on_page(f_element.technology_title())
    general_action.scroll_page('320')
    general_action.check_element_on_page(f_element.technology_text_block())

    general_action.scroll_page('1050')
    general_action.check_element_on_page(f_element.troubleshooting_title())
    general_action.check_element_on_page(f_element.troubleshooting_text_block())

    general_action.scroll_page('1800')
    general_action.check_element_on_page(f_element.have_question_button())
    general_action.check_element_on_page(f_element.try_it_now_button())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on FAQ page')
@allure.story('FAQ page button')
def test_buttons(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    f_element = FaqPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#faq')

    general_action.scroll_page('1800')
    general_action.click_on_button(f_element.try_it_now_button())

    general_action.check_url(page_url + '#signup')
