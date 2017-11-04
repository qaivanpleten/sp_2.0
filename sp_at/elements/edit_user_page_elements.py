from selenium.webdriver.support.select import Select


class EditUsersPageElements:
    def __init__(self, driver):
        self.driver = driver

    def username_block(self):
        return self.driver.find_element_by_id('username')

    def username_input(self):
        return self.driver.find_element_by_xpath('//*[@id="username"]/div/input')

    def first_name_block(self):
        return self.driver.find_element_by_id('firstname')

    def first_name_input(self):
        return self.driver.find_element_by_xpath('//*[@id="firstname"]/div/input')

    def last_name_block(self):
        return self.driver.find_element_by_id('lastname')

    def last_name_input(self):
        return self.driver.find_element_by_xpath('//*[@id="lastname"]/div/input')

    # email block
    def email_block(self):
        return self.driver.find_element_by_id('emails')

    def email_input(self):
        return self.driver.find_element_by_xpath('//*[@id="emails"]/div/span/form/div[1]/input')

    def second_email_input(self):
        return self.driver.find_element_by_xpath('//*[@id="emails"]/div/span/form[2]/div[1]/input')

    def add_email_button(self):
        return self.driver.find_element_by_xpath('//*[@id="emails"]/div/span/form/div[2]/span/a')

    def delete_email_button(self):
        return self.driver.find_element_by_xpath('//*[@id="emails"]/div/span/form[2]/div[2]/span[2]/a/i')

    def email_label(self):
        return self.driver.find_element_by_xpath('//*[@id="emails"]/div/span/form[1]/div[2]/div/select')

    # phone block
    def phone_block(self):
        return self.driver.find_element_by_id('telephones')

    def phone_input(self):
        return self.driver.find_element_by_xpath('//*[@id="telephones"]/div/span/form/div[1]/input')

    def add_phone_button(self):
        return self.driver.find_element_by_xpath('//*[@id="telephones"]/div/span/form/div[2]/span/a/i')

    # data block
    def data_block(self):
        return self.driver.find_element_by_id('basic-data')

    def role_select(self):
        return self.driver.find_element_by_class_name('sp-select-role')

    def suspend_button(self):
        return self.driver.find_element_by_xpath('//*[@id="user-actions"]/button[1]')

    def delete_button(self):
        return self.driver.find_element_by_xpath('//*[@id="user-actions"]/button[2]')

    def back_button(self):
        return self.driver.find_element_by_xpath('//*[@id="actions-panel"]/span[1]/a/span')

    # activity block
    def activity_block(self):
        return self.driver.find_element_by_id('activity-region')

    def search_activity_input(self):
        return self.driver.find_element_by_xpath('//*[@id="filter-form"]/div/input')

    def find_button(self):
        return self.driver.find_element_by_xpath('//*[@id="filter-form"]/div/button')

    def first_id_in_the_list(self):
        return self.driver.find_element_by_xpath('//*[@id="list-region"]/table/tbody/tr/td[1]')

    def session_id(self):
        return "9bowj66"
