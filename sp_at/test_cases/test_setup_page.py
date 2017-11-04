import time

import allure
import pytest

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.elements.setup_page_elements import SetupPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check elements on Setup page')
@allure.story('General elements')
def test_general_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()

    general_action = GeneralActions(fixture_webdriver)
    mp_element = MainPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#setup')

    # check header elements
    general_action.check_element_on_page(mp_element.logo())
    general_action.check_element_on_page(mp_element.signup_button())
    general_action.check_element_on_page(mp_element.login_button())
    general_action.check_element_on_page(mp_element.hamburger_menu_button())

    # # check footer elements
    # general_action.check_element_on_page(mp_element.footer_whyus())
    # general_action.check_element_on_page(mp_element.footer_company())
    # general_action.check_element_on_page(mp_element.footer_career())
    # general_action.check_element_on_page(mp_element.footer_faq())
    # general_action.check_element_on_page(mp_element.footer_contact())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check elements on Setup page')
@allure.story('Setup page elements')
def test_page_elements(fixture_webdriver):
    page_url = MainPageElements(fixture_webdriver).url()

    general_action = GeneralActions(fixture_webdriver)
    setup_element = SetupPageElements(fixture_webdriver)
    general_action.open_page_by_url(page_url + '#setup')

    general_action.check_element_on_page(setup_element.quick_start_block())
    general_action.check_element_on_page(setup_element.quick_start_picture())

    general_action.scroll_page('400')
    general_action.check_element_on_page(setup_element.mobile_app_block())
    general_action.check_element_on_page(setup_element.mobile_app_picture())

    time.sleep(1)
    general_action.scroll_page('1000')
    general_action.check_element_on_page(setup_element.desktop_app_block())
    general_action.check_element_on_page(setup_element.desktop_app_picture())

    time.sleep(1)
    general_action.scroll_page('1500')
    general_action.check_element_on_page(setup_element.login_block())
    general_action.check_element_on_page(setup_element.login_picture())

    time.sleep(1)
    general_action.scroll_page('2000')
    general_action.check_element_on_page(setup_element.add_user_block())
    general_action.check_element_on_page(setup_element.add_user_picture())

    time.sleep(1)
    general_action.scroll_page('2500')
    general_action.check_element_on_page(setup_element.go_to_user_dashboard_block())
    general_action.check_element_on_page(setup_element.go_to_user_dashboard_picture())

    time.sleep(1)
    general_action.scroll_page('3000')
    general_action.check_element_on_page(setup_element.add_single_user_block())
    general_action.check_element_on_page(setup_element.add_single_user_picture())

    time.sleep(1)
    general_action.scroll_page('3500')
    general_action.check_element_on_page(setup_element.import_user_block())
    general_action.check_element_on_page(setup_element.import_user_picture())

    time.sleep(1)
    general_action.scroll_page('4000')
    general_action.check_element_on_page(setup_element.verify_user_block())
    general_action.check_element_on_page(setup_element.verify_user_picture())

    time.sleep(1)
    general_action.scroll_page('4500')
    general_action.check_element_on_page(setup_element.onboarding_post_block())
    general_action.check_element_on_page(setup_element.onboarding_email_picture())

    time.sleep(1)
    general_action.scroll_page('5000')
    general_action.check_element_on_page(setup_element.onboarding_email_block())
    general_action.check_element_on_page(setup_element.onboarding_post_picture())

    time.sleep(1)
    general_action.scroll_page('5500')
    general_action.check_element_on_page(setup_element.user_setup_complete_block())
    general_action.check_element_on_page(setup_element.user_setup_complete_picture())

    time.sleep(1)
    general_action.scroll_page('6000')
    general_action.check_element_on_page(setup_element.gsuite_setup_block())
    general_action.check_element_on_page(setup_element.gsuite_setup_picture())

    time.sleep(1)
    general_action.scroll_page('6500')
    general_action.check_element_on_page(setup_element.gsuite_admin_block())
    general_action.check_element_on_page(setup_element.gsuite_admin_picture())

    time.sleep(1)
    general_action.scroll_page('7100')
    general_action.check_element_on_page(setup_element.select_setup_sso_block())
    general_action.check_element_on_page(setup_element.select_setup_sso_picture())

    time.sleep(1)
    general_action.scroll_page('7500')
    general_action.check_element_on_page(setup_element.select_checkbox_block())
    general_action.check_element_on_page(setup_element.select_checkbox_picture())

    time.sleep(1)
    general_action.scroll_page('8000')
    general_action.check_element_on_page(setup_element.download_sso_block())
    general_action.check_element_on_page(setup_element.download_sso_picture())

    time.sleep(1)
    general_action.scroll_page('8700')
    general_action.check_element_on_page(setup_element.upload_certificate_block())
    general_action.check_element_on_page(setup_element.upload_certificate_picture())

    time.sleep(1)
    general_action.scroll_page('9000')
    general_action.check_element_on_page(setup_element.add_signin_url_block())
    general_action.check_element_on_page(setup_element.add_signin_url_picture())

    time.sleep(1)
    general_action.scroll_page('9600')
    general_action.check_element_on_page(setup_element.add_signout_url_block())
    general_action.check_element_on_page(setup_element.add_signout_url_picture())

    time.sleep(1)
    general_action.scroll_page('10200')
    general_action.check_element_on_page(setup_element.add_change_pass_url_block())
    general_action.check_element_on_page(setup_element.add_change_pass_url_picture())

    time.sleep(1)
    general_action.scroll_page('11200')
    general_action.check_element_on_page(setup_element.click_save_block())
    general_action.check_element_on_page(setup_element.click_save_picture())

    time.sleep(1)
    general_action.scroll_page('11650')
    general_action.check_element_on_page(setup_element.gsuite_complete_block())
    general_action.check_element_on_page(setup_element.gsuite_complete_picture())
