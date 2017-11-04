class UsersPageElements:
    def __init__(self, driver):
        self.driver = driver

    def users_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/h1')

    def list_of_emails(self):
        return self.driver.find_element_by_id('users-holder')

    def content_left(self):
        return self.driver.find_element_by_id('content_left')

    def content_right(self):
        return self.driver.find_element_by_id('content_right')

    def new_user_button(self):
        return self.driver.find_element_by_id('add-user')

    def import_user_button(self):
        return self.driver.find_element_by_id('add-users')

    # new user popup

    def firstname_input(self):
        return self.driver.find_element_by_id('user-given_name')

    def lastname_input(self):
        return self.driver.find_element_by_id('user-surname')

    def email_input(self):
        return self.driver.find_element_by_id('user-username')

    def country_code_input(self):
        return self.driver.find_element_by_id('country-code')

    def phone_number_input(self):
        return self.driver.find_element_by_id('user-telephone')

    def submit_button(self):
        return self.driver.find_element_by_xpath('//*[@id="dialog-region"]/div/form/button')

    # users block

    def delete_first_user_button(self):
        return self.driver.find_element_by_xpath('//*[@id="user-actions"]/button')

    def confirm_delete_button(self):
        return self.driver.find_element_by_id('dialog-confirm')

    def cancel_delete_button(self):
        return self.driver.find_element_by_id('dialog-cancel')

    def sonik_pass_domen(self):
        return "@selenium.dp"

    def admin_email(self):
        return "admin@selenium.bb"

    def first_user_in_list(self):
        return self.driver.find_element_by_xpath('//*[@id="users-region"]/table/tbody/tr/td[1]')
