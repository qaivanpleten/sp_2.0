import time
from faker import Faker

from sp_at.actions.general_actions import GeneralActions
from sp_at.actions.login_actions import LoginActions
from sp_at.elements.edit_user_page_elements import EditUsersPageElements
from sp_at.elements.users_page_elements import UsersPageElements
from sp_at.elements.welcome_page_elements import WelcomePageElements


class UsersPageActions:
    def __init__(self, driver):
        self.driver = driver

    def open_users_page(self):
        LoginActions(self.driver).login_full_case(UsersPageElements(self.driver).admin_email())
        GeneralActions(self.driver).click_on_button(WelcomePageElements(self.driver).dashboard_button())

    def fill_new_user_form(self, firsname=None, lastname=None, email=None, country_code=None, phone=None):
        form_element = UsersPageElements(self.driver)

        GeneralActions(self.driver).click_on_button(form_element.new_user_button())
        form_element.firstname_input().send_keys(firsname)
        form_element.lastname_input().send_keys(lastname)
        form_element.email_input().send_keys(email)
        form_element.country_code_input().click()
        form_element.country_code_input().clear()
        form_element.country_code_input().send_keys(country_code)
        form_element.phone_number_input().send_keys(phone)

        GeneralActions(self.driver).click_on_button(form_element.submit_button())
        time.sleep(2)

    def open_edit_user_page(self):
        domen = UsersPageElements(self.driver).sonik_pass_domen()
        fake = Faker()
        email = fake.first_name() + domen

        UsersPageActions(self.driver).open_users_page()
        UsersPageActions(self.driver).fill_new_user_form("john", "doe", email, "+38", "0671112223")
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="users-region"]/table/tbody/tr[2]/td[2]/a/i').click()
        time.sleep(5)

    def confirm_user_deleting(self):
        UsersPageElements(self.driver).delete_first_user_button().click()
        UsersPageElements(self.driver).confirm_delete_button().click()
        time.sleep(3)

    def cancel_user_deleting(self):
        UsersPageElements(self.driver).delete_first_user_button().click()
        UsersPageElements(self.driver).cancel_delete_button().click()
        time.sleep(2)

    def open_admin_details_page(self):
        UsersPageActions(self.driver).open_users_page()
        self.driver.find_element_by_xpath('//*[@id="user-actions"]/a/i').click()
