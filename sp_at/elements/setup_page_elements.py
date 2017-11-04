class SetupPageElements:
    def __init__(self, driver):
        self.driver = driver

    def quick_start_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section1"]/div[1]/div[1]')

    def quick_start_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section1"]/div[1]/div[2]')

    def mobile_app_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section1"]/div[2]/div[1]')

    def mobile_app_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section1"]/div[2]/div[2]')

    def desktop_app_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section3"]/div[1]/div[1]')

    def desktop_app_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section3"]/div[1]/div[2]')

    def login_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section3"]/div[2]/div[1]')

    def login_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section3"]/div[2]/div[2]')

    def add_user_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[1]/div[1]')

    def add_user_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[1]/div[2]')

    def go_to_user_dashboard_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[2]/div[1]')

    def go_to_user_dashboard_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[2]/div[2]')

    def add_single_user_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[3]/div[1]')

    def add_single_user_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[3]/div[2]')

    def import_user_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[4]/div[1]')

    def import_user_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[4]/div[2]')

    def verify_user_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[5]/div[1]')

    def verify_user_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[5]/div[2]')

    def onboarding_post_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[6]/div[1]')

    def onboarding_post_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[6]/div[2]')

    def onboarding_email_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[7]/div[1]')

    def onboarding_email_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[7]/div[2]')

    def user_setup_complete_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[8]/div[1]')

    def user_setup_complete_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section4"]/div[8]/div[2]')

    def gsuite_setup_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[1]/div[1]')

    def gsuite_setup_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[1]/div[2]')

    def gsuite_admin_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[2]/div[1]')

    def gsuite_admin_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[2]/div[2]')

    def select_setup_sso_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[3]/div[1]/div')

    def select_setup_sso_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[3]/div[2]')

    def select_checkbox_sso_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[4]/div[1]/div')

    def select_checkbox_sso_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[4]/div[2]')

    def download_sso_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[5]/div[1]/div')

    def download_sso_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[5]/div[2]')

    def upload_certificate_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[6]/div[1]')

    def upload_certificate_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[6]/div[2]')

    def add_signin_url_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[7]/div[1]')

    def add_signin_url_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[7]/div[2]')

    def add_signout_url_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[8]/div[1]')

    def add_signout_url_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[8]/div[2]')

    def add_change_pass_url_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[9]/div[1]')

    def add_change_pass_url_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[9]/div[2]')

    def select_checkbox_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[10]/div[1]/div')

    def select_checkbox_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[10]/div[2]')

    def click_save_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[11]/div[1]')

    def click_save_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[11]/div[2]')

    def gsuite_complete_block(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[12]/div[1]')

    def gsuite_complete_picture(self):
        return self.driver.find_element_by_xpath('//*[@id="section5"]/div[12]/div[2]')
