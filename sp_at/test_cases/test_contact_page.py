import allure
import pytest

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.contact_us_page_elements import ContactPageElements
from sp_at.elements.main_page_elements import MainPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Contact page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#contact')

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
@allure.feature('Check elements on Contact page')
@allure.story('Contact page elements')
def test_page_element(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    contact_element = ContactPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#contact')

    general_action.check_element_on_page(contact_element.contact_title())
    general_action.check_element_on_page(contact_element.partnership_email())
    general_action.check_element_on_page(contact_element.support_email())
    general_action.check_element_on_page(contact_element.sales_email())
    general_action.check_element_on_page(contact_element.general_email())
    general_action.check_element_on_page(contact_element.try_it_button())
    general_action.check_element_on_page(contact_element.faq_button())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Contact page')
@allure.story('Contact page button')
def test_button(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    contact_element = ContactPageElements(fixture_webdriver)

    general_action.open_page_by_url(page_url + '#contact')
    general_action.click_on_button(contact_element.faq_button())
    general_action.check_url(page_url + '#faq')

    general_action.open_page_by_url(page_url + '#contact')
    general_action.click_on_button(contact_element.try_it_button())
    general_action.check_url(page_url + '#signup')
