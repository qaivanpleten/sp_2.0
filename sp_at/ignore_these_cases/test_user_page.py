import time

import allure
import pytest
from faker import Faker

from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.users_page_actions import UsersPageActions
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.elements.users_page_elements import UsersPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check User page features')
@allure.story('Check general elements')
def test_check_elements(fixture_webdriver):
    users_element = UsersPageElements(fixture_webdriver)
    general_actions = GeneralActions(fixture_webdriver)

    UsersPageActions(fixture_webdriver).open_users_page()
    time.sleep(10)

    general_actions.check_url(MainPageElements(fixture_webdriver).url() + "#users")
    general_actions.check_element_on_page(users_element.users_title())
    general_actions.check_element_on_page(users_element.list_of_emails())
    general_actions.check_element_on_page(users_element.content_left())
    general_actions.check_element_on_page(users_element.content_right())


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check User page features')
@allure.story('Add new user')
def test_add_user(fixture_webdriver):
    action = UsersPageActions(fixture_webdriver)
    fake = Faker()
    email = fake.first_name() + UsersPageElements(fixture_webdriver).sonik_pass_domen()

    action.open_users_page()
    action.fill_new_user_form("john", "doe", email, "+38", "0671112223")
    assert email in \
           fixture_webdriver.find_element_by_xpath(
               '//*[@id="users-region"]/table/tbody/tr[2]/td[1]').get_attribute(
               "textContent")

    fixture_webdriver.refresh()
    time.sleep(3)

    action.confirm_user_deleting()


# def test_add_user_with_invalid_data(fixture_webdriver):
#     fake = Faker()
#     email = fake.email()
#     UsersPageActions(fixture_webdriver).open_users_page()
#     UsersPageActions(fixture_webdriver).fill_new_user_form("john", "doe", email, "+38", "0671112223")
#
#     # there should be an error message. functional is in progress


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check User page features')
@allure.story('Delete user')
def test_delete_user(fixture_webdriver):
    action = UsersPageActions(fixture_webdriver)
    admin_email = UsersPageElements(fixture_webdriver).admin_email()
    fake = Faker()
    email = fake.first_name() + UsersPageElements(fixture_webdriver).sonik_pass_domen()

    action.open_users_page()
    action.fill_new_user_form("john", "doe", email, "+38", "0671112223")
    fixture_webdriver.refresh()
    time.sleep(2)
    action.confirm_user_deleting()

    assert admin_email in \
           fixture_webdriver.find_element_by_xpath('//*[@id="users-region"]/table/tbody/tr/td[1]').get_attribute(
               "textContent")


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check User page features')
@allure.story('Cancel user deleting')
def test_cancel_deleting(fixture_webdriver):
    action = UsersPageActions(fixture_webdriver)
    fake = Faker()
    email = fake.first_name() + UsersPageElements(fixture_webdriver).sonik_pass_domen()

    action.open_users_page()
    action.fill_new_user_form("john", "doe", email, "+38", "0671112223")
    fixture_webdriver.refresh()
    time.sleep(2)
    action.cancel_user_deleting()

    assert email in \
           fixture_webdriver.find_element_by_xpath('//*[@id="users-region"]/table/tbody/tr/td[1]').get_attribute(
               "textContent")

    fixture_webdriver.refresh()
    time.sleep(2)
    action.confirm_user_deleting()

# def test_import_users(fixture_webdriver):
#     UsersPageActions(fixture_webdriver).open_users_page()
#     UsersPageElements(fixture_webdriver).import_user_button().click()
#     # add this test later
