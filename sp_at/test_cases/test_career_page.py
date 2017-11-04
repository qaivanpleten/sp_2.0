import allure
import pytest

from sp_at.actions.career_page_actions import CareerPageActions
from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.career_page_elements import CareerPageElements
from sp_at.elements.main_page_elements import MainPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Career page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#careers')

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
@allure.feature('Check elements on Career page')
@allure.story('Career page elements')
def test_career_page(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    car_action = CareerPageActions(fixture_webdriver)
    car_element = CareerPageElements(fixture_webdriver)

    general_action.open_page_by_url(page_url + '#careers')

    car_action.check_list_of_elements(1, 5)
    general_action.check_element_on_page(car_element.faq_button())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Career page')
@allure.story('Career page buttons')
def test_button(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()
    general_action = GeneralActions(fixture_webdriver)
    car_element = CareerPageElements(fixture_webdriver)

    general_action.open_page_by_url(page_url + '#careers')
    general_action.click_on_button(car_element.faq_button())
    general_action.check_url(page_url + '#faq')
