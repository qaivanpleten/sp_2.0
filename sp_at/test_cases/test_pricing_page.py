import time

import allure
import pytest

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.elements.pricing_page_elements import PricingPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Pricing page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#pricing')
    time.sleep(3)

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
@allure.feature('Check elements on Pricing page')
@allure.story('Pricing page elements')
def test_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    pricing_element = PricingPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#pricing')

    general_action.check_element_on_page(pricing_element.pricing_title())
    general_action.check_element_on_page(pricing_element.text())
    general_action.check_element_on_page(pricing_element.contact_button())
    general_action.check_element_on_page(pricing_element.try_button())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Pricing page')
@allure.story('Pricing page buttons')
def test_button(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    pricing_element = PricingPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#pricing')

    general_action.click_on_button(pricing_element.try_button())
    general_action.check_url(page_url + '#signup')
