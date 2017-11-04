class MainPageElements:
    def __init__(self, driver):
        self.driver = driver

    def url(self):
        return 'http://console.sonikpass.com/'

    # general elements, footer
    def logo(self):
        return self.driver.find_element_by_xpath('//*[@id="app-container"]/a/div[2]')

    def signup_button(self):
        return self.driver.find_element_by_id('signup_link')

    def login_button(self):
        return self.driver.find_element_by_xpath('//*[@id="app-container"]/div[2]/button')

    def hamburger_menu_button(self):
        return self.driver.find_element_by_xpath('//*[@id="app-container"]/div[1]/div')

    # intro block
    def page_title(self):
        return self.driver.find_element_by_xpath('//*[@id="intro"]/div/div/div[1]/h1')

    def tryitnow_button(self):
        return self.driver.find_element_by_xpath('//*[@id="intro"]/div/div/div[2]/p/button')

    def howitworks_button(self):
        return self.driver.find_element_by_xpath('//*[@id="intro"]/div/div/div[2]/p/a/button')

    # how it works (problem) block
    def howitworks_title(self):
        return self.driver.find_element_by_xpath('//*[@id="problem"]/div/div/div/h2')

    def ten_reason_to_love_button(self):
        return self.driver.find_element_by_xpath('//*[@id="problem"]/div/div/div/div[3]/a/button')

    # solution block
    def usability_and_security_title(self):
        return self.driver.find_element_by_xpath('//*[@id="solution"]/div[1]/div/h2')

    def faq_button(self):
        return self.driver.find_element_by_xpath('//*[@id="solution"]/div[1]/div/p/a/button')

    # usages
    def where_can_ibe_used_button(self):
        return self.driver.find_element_by_xpath('//*[@id="usagecases"]/div/div[1]/h2')

    def slider_left_button(self):
        return self.driver.find_element_by_xpath('//*[@id="usagecases"]/div/div[1]/ul[2]/li[1]')

    def slider_right_button(self):
        return self.driver.find_element_by_xpath('//*[@id="usagecases"]/div/div[1]/ul[2]/li[2]')

    def slider_mask(self):
        return self.driver.find_element_by_xpath('//*[@id="usagecases"]/div/div[1]/ul[1]/li[3]')

    def slider_internet(self):
        return self.driver.find_element_by_xpath('//*[@id="usagecases"]/div/div[1]/ul[1]/li[1]')

    def slider_pad(self):
        return self.driver.find_element_by_xpath('//*[@id="usagecases"]/div/div[1]/ul[1]/li[2]')

    # partner
    def get_in_touch_title(self):
        return self.driver.find_element_by_xpath('//*[@id="partner"]/div/div[2]/h1')

    def meet_team_button(self):
        return self.driver.find_element_by_xpath('//*[@id="partner"]/div/div[2]/a[1]/button')

    def info_sonikpass_button(self):
        return self.driver.find_element_by_xpath('//*[@id="partner"]/div/div[2]/a[2]/button')

    # footer
    def footer_whyus(self):
        return self.driver.find_element_by_xpath('//*[@id="quick_links"]/a[1]')

    def footer_company(self):
        return self.driver.find_element_by_xpath('//*[@id="quick_links"]/a[2]')

    def footer_career(self):
        return self.driver.find_element_by_xpath('//*[@id="quick_links"]/a[3]')

    def footer_faq(self):
        return self.driver.find_element_by_xpath('//*[@id="quick_links"]/a[4]')

    def footer_contact(self):
        return self.driver.find_element_by_xpath('//*[@id="quick_links"]/a[5]')

    # hamburger menu

    def hamburger_faq(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[1]/a')

    def hamburger_about(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[2]/a')

    def hamburger_careers(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[3]/a')

    def hamburger_contact(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[4]/a')

    def hamburger_usecases(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[5]/a')

    def hamburger_pricing(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[6]/a')

    def hamburger_integration(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[7]/a')

    def hamburger_setup(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[8]/a')

    def hamburger_install(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[9]/a')

    def hamburger_login(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[10]/a')

    def hamburger_signup(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[11]/a')

    def hamburger_why(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[12]/a')

    def hamburger_privacy(self):
        return self.driver.find_element_by_xpath('//*[@id="slideout-menu"]/li[13]/a')

    # sidebar buttons

    def sidebar_intro(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/ul/li[1]/a')

    def sidebar_problem(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/ul/li[2]/a')

    def sidebar_solution(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/ul/li[3]/a')

    def sidebar_usagecases(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/ul/li[4]/a')

    def sidebar_partner(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/ul/li[5]/a')

    def sidebar(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/ul')

    # popups

    def login_dialog(self):
        return self.driver.find_element_by_xpath('//*[@class="page-try"]/div[2]')

    def dialog_title(self):
        return self.driver.find_element_by_id('dialog-title')

    def dialog_username_input(self):
        return self.driver.find_element_by_id('dialog-username-input')

    def dialog_next_button(self):
        return self.driver.find_element_by_id('dialog-confirm')

    def dialog_cancel_button(self):
        return self.driver.find_element_by_id('dialog-cancel')
