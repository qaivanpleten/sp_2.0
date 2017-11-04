class SignUpPageElements:
    def __init__(self, driver):
        self.driver = driver

    def signup_title(self):
        return self.driver.find_element_by_xpath('//*[@id="section0"]/div/div[1]/div')

    def text_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section0"]/div/div[1]')

    def fname_title(self):
        return self.driver.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div/form/div[1]/label')

    def fname_input(self):
        return self.driver.find_element_by_id('user-given_name')

    def lname_title(self):
        return self.driver.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div/form/div[2]/label')

    def lname_input(self):
        return self.driver.find_element_by_id('user-surname')

    def email_title(self):
        return self.driver.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div/form/div[3]/label')

    def email_input(self):
        return self.driver.find_element_by_id('user-username')

    def phone_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div/form/div[4]/label')

    def country_code_input(self):
        return self.driver.find_element_by_id('country-code')

    def phone_input(self):
        return self.driver.find_element_by_id('user-telephone')

    def create_account_button(self):
        return self.driver.find_element_by_xpath('//*[@id="section0"]/div/div[2]/div/form/button')
