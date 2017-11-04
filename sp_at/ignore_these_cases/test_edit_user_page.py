import time

import allure
import pytest
from faker import Faker
from sp_at.actions.edit_users_page_actions import EditUsersPageActions
from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.users_page_actions import UsersPageActions
from sp_at.elements.edit_user_page_elements import EditUsersPageElements
from sp_at.elements.users_page_elements import UsersPageElements


@pytest.allure.severity(pytest.allure.severity_level.MINOR)
@allure.feature('Check user page features')
@allure.story('Check general elements')
def test_page_element(fixture_webdriver):
    general_action = GeneralActions(fixture_webdriver)
    page_element = EditUsersPageElements(fixture_webdriver)
    UsersPageActions(fixture_webdriver).open_edit_user_page()

    general_action.check_element_on_page(page_element.username_block())
    general_action.check_element_on_page(page_element.first_name_block())
    general_action.check_element_on_page(page_element.last_name_block())
    general_action.check_element_on_page(page_element.email_block())
    general_action.check_element_on_page(page_element.phone_block())
    general_action.check_element_on_page(page_element.data_block())
    general_action.check_element_on_page(page_element.suspend_button())
    general_action.check_element_on_page(page_element.delete_button())
    general_action.check_element_on_page(page_element.activity_block())

    EditUsersPageActions(fixture_webdriver).delete_user()


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Delete user')
def test_delete_user_confirm(fixture_webdriver):
    element = UsersPageElements(fixture_webdriver)

    UsersPageActions(fixture_webdriver).open_edit_user_page()
    EditUsersPageActions(fixture_webdriver).delete_user()

    assert element.admin_email() in element.first_user_in_list().get_attribute(
        "textContent"), "First email in the list should be admin@selenium.dp"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Cancel user deleting')
def test_delete_user_cancel(fixture_webdriver):
    element = UsersPageElements(fixture_webdriver)
    UsersPageActions(fixture_webdriver).open_edit_user_page()
    EditUsersPageActions(fixture_webdriver).cancel_deleting_user()

    assert element.admin_email() in \
           fixture_webdriver.find_element_by_xpath('//*[@id="users-region"]/table/tbody/tr[2]/td[1]').get_attribute(
               "textContent"), "Second email in the list should be admin@selenium.dp"

    UsersPageActions(fixture_webdriver).confirm_user_deleting()


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Suspend user')
def test_suspend_user(fixture_webdriver):
    element = UsersPageElements(fixture_webdriver)

    UsersPageActions(fixture_webdriver).open_edit_user_page()
    EditUsersPageActions(fixture_webdriver).suspend_user()

    assert element.admin_email() in element.first_user_in_list().get_attribute(
        "textContent"), "First email in the list should be admin@selenium.dp"


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Change user role')
def test_change_role(fixture_webdriver):
    UsersPageActions(fixture_webdriver).open_edit_user_page()
    EditUsersPageActions(fixture_webdriver).change_role()
    EditUsersPageActions(fixture_webdriver).delete_user()


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Change username')
def test_change_username(fixture_webdriver):
    element = UsersPageElements(fixture_webdriver)

    UsersPageActions(fixture_webdriver).open_edit_user_page()
    EditUsersPageActions(fixture_webdriver).change_username('Arename')

    time.sleep(2)
    assert 'Arename' in \
           element.first_user_in_list().get_attribute(
               "textContent"), "First username in the list should be Arename"
    UsersPageActions(fixture_webdriver).confirm_user_deleting()


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Change first name')
def test_change_first_name(fixture_webdriver):
    action = EditUsersPageActions(fixture_webdriver)

    UsersPageActions(fixture_webdriver).open_edit_user_page()
    action.change_first_name('John')

    assert 'John' in (EditUsersPageElements(fixture_webdriver).first_name_input()).get_attribute(
        'value'), "First name should be John"

    action.delete_user()


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Change last name')
def test_change_last_name(fixture_webdriver):
    action = EditUsersPageActions(fixture_webdriver)

    UsersPageActions(fixture_webdriver).open_edit_user_page()
    action.change_last_name('Black')

    assert 'Black' in (EditUsersPageElements(fixture_webdriver).last_name_input()).get_attribute(
        'value'), "Last name should be Black"

    action.delete_user()


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Change email')
def test_change_email(fixture_webdriver):
    action = EditUsersPageActions(fixture_webdriver)

    UsersPageActions(fixture_webdriver).open_edit_user_page()
    action.change_email('change')

    assert 'change' + UsersPageElements(fixture_webdriver).sonik_pass_domen() in (
        EditUsersPageElements(fixture_webdriver).email_input()).get_attribute('value'), "The email value is wrong"

    action.delete_user()


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Change phone number')
def test_change_phone_number(fixture_webdriver):
    action = EditUsersPageActions(fixture_webdriver)

    UsersPageActions(fixture_webdriver).open_edit_user_page()
    action.change_phone_number('0111222333')

    assert '0111222333' in (
        EditUsersPageElements(fixture_webdriver).phone_input()).get_attribute(
        'value'), 'The phone number should be 0111222333'

    action.delete_user()


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Add new email')
def test_add_emails(fixture_webdriver):
    UsersPageActions(fixture_webdriver).open_edit_user_page()
    EditUsersPageActions(fixture_webdriver).add_email()
    EditUsersPageActions(fixture_webdriver).delete_user()


# def test_delete_email(fixture_webdriver):
# #skip this one until fe will be fixed
#     UsersPageActions(fixture_webdriver).open_edit_user_page()
#     EditUsersPageActions(fixture_webdriver).delete_email()
#     EditUsersPageActions(fixture_webdriver).delete_user()

@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Add new phone number')
def test_add_phone_number(fixture_webdriver):
    UsersPageActions(fixture_webdriver).open_edit_user_page()
    EditUsersPageActions(fixture_webdriver).add_phone_number()
    EditUsersPageActions(fixture_webdriver).delete_user()


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@allure.feature('Check user page features')
@allure.story('Search session ID')
def test_search_session_id(fixture_webdriver):
    UsersPageActions(fixture_webdriver).open_admin_details_page()

    session_id = EditUsersPageElements(fixture_webdriver).session_id()
    EditUsersPageActions(fixture_webdriver).search_session_id(session_id)
    time.sleep(5)

    assert session_id in EditUsersPageElements(fixture_webdriver).first_id_in_the_list().get_attribute(
        "textContent"), "The session ID is wrogn"
