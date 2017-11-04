import time

from faker import Faker

from sp_at.elements.edit_user_page_elements import EditUsersPageElements
from sp_at.elements.users_page_elements import UsersPageElements
from selenium import webdriver
from selenium.webdriver.support.select import Select as WebDriverSelect


class EditUsersPageActions:
    def __init__(self, driver):
        self.driver = driver

    def delete_user(self):
        EditUsersPageElements(self.driver).delete_button().click()
        UsersPageElements(self.driver).confirm_delete_button().click()
        time.sleep(5)

    def cancel_deleting_user(self):
        EditUsersPageElements(self.driver).delete_button().click()
        UsersPageElements(self.driver).cancel_delete_button().click()
        time.sleep(1)
        EditUsersPageElements(self.driver).back_button().click()

    def suspend_user(self):
        EditUsersPageElements(self.driver).suspend_button().click()
        time.sleep(3)

    def change_username(self, name):
        username = EditUsersPageElements(self.driver).username_input()
        username.click()
        username.clear()
        username.send_keys(name)

        EditUsersPageElements(self.driver).back_button().click()

    def change_role(self):
        dropdown = EditUsersPageElements(self.driver).role_select()
        select_list = WebDriverSelect(dropdown)
        select_list.select_by_value('0')
        selected_option = select_list.first_selected_option.text
        assert selected_option == 'admin', "Selected option should be Admin"

    def change_first_name(self, name):
        fname = EditUsersPageElements(self.driver).first_name_input()
        fname.click()
        fname.clear()
        fname.send_keys(name)

        EditUsersPageElements(self.driver).username_input().click()
        time.sleep(1)

    def change_last_name(self, name):
        lname = EditUsersPageElements(self.driver).last_name_input()
        lname.click()
        lname.clear()
        lname.send_keys(name)

        EditUsersPageElements(self.driver).username_input().click()
        time.sleep(1)

    def change_email(self, name):
        email = EditUsersPageElements(self.driver).email_input()
        email_name = name + UsersPageElements(self.driver).sonik_pass_domen()
        email.click()
        email.clear()
        email.send_keys(email_name)

        EditUsersPageElements(self.driver).username_input().click()
        time.sleep(1)

    def change_phone_number(self, number):
        phone = EditUsersPageElements(self.driver).phone_input()
        phone.click()
        phone.clear()
        phone.send_keys(number)

        EditUsersPageElements(self.driver).username_input().click()
        time.sleep(1)

    def add_email(self):
        a = 2
        for x in range(3):
            email = "bla" + str(a) + UsersPageElements(self.driver).sonik_pass_domen()
            add_button = EditUsersPageElements(self.driver).add_email_button()
            username = EditUsersPageElements(self.driver).username_input()

            add_button.click()

            email_input = self.driver.find_element_by_xpath(
                '//*[@id="emails"]/div/span/form[' + str(a) + ']/div[1]/input')
            email_input.click()
            email_input.send_keys(email)
            username.click()

            assert email in email_input.get_attribute('value')

            a += 1
            x += 1

            time.sleep(3)

    def change_email_priority(self):
        element = EditUsersPageElements(self.driver)
        email = "bla" + UsersPageElements(self.driver).sonik_pass_domen()
        add_button = element.add_email_button()
        username = element.username_input()
        label = WebDriverSelect(element.email_label())
        value = 1

        add_button.click()
        email_input = element.second_email_input()

        email_input.click()
        email_input.send_keys(email)
        username.click()

        for x in range(5):
            label.select_by_value(str(value))
            selected_option = label.first_selected_option.text
            if value == 0:
                assert selected_option == 'Primary', "Selected option should be Primary"

            elif value == 1:
                assert selected_option == 'Secondary', "Selected option should be Secondary"

            elif value == 2:
                assert selected_option == 'Work', "Selected option should be Work"

            elif value == 3:
                assert selected_option == 'Personal', "Selected option should be Personal"

            elif value == 4:
                assert selected_option == 'Other', "Selected option should be Other"

            value += 1

    def delete_email(self):
        element = EditUsersPageElements(self.driver)

        email = "bla" + UsersPageElements(self.driver).sonik_pass_domen()
        add_button = element.add_email_button()
        username = element.username_input()

        add_button.click()

        email_input = self.driver.find_element_by_xpath('//*[@id="emails"]/div/span/form[2]/div[1]/input')
        email_input.click()
        email_input.send_keys(email)
        username.click()
        time.sleep(3)
        element.delete_email_button().click()

    def add_phone_number(self):
        a = 2
        for x in range(3):
            number = Faker().phone_number()
            add_button = EditUsersPageElements(self.driver).add_phone_button()
            username = EditUsersPageElements(self.driver).username_input()

            add_button.click()
            phone_input = self.driver.find_element_by_xpath(
                '//*[@id="telephones"]/div/span/form[' + str(a) + ']/div[1]/input')

            phone_input.click()
            phone_input.send_keys(str(number))
            username.click()
            time.sleep(5)
            # assert phone_input.get_attribute('value') == str(number)

            a += 1
            x += 1

    def search_session_id(self, session_id):
        element = EditUsersPageElements(self.driver)

        element.search_activity_input().click()
        element.search_activity_input().clear()
        element.search_activity_input().send_keys(session_id)

        element.find_button().click()
