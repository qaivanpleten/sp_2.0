from selenium.webdriver.remote.webdriver import WebDriver


class Header:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logo = self.driver.find_element_by_xpath('//*[@id="app-container"]/a/div[2]')
        self.signup_button = self.driver.find_element_by_id('signup_link')
        self.login_button = self.driver.find_element_by_xpath('//*[@id="app-container"]/div[2]/button')
        self.hamburger_menu_button = self.driver.find_element_by_xpath('//*[@id="app-container"]/div[1]/div')

    def present(self) -> bool:
        for element in (self.logo, self.signup_button, self.login_button, self.hamburger_menu_button):
            if not element.is_displayed():
                return False

        return True


class Footer:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.footer_whyus = self.driver.find_element_by_xpath('//*[@id="quick_links"]/a[1]')
        self.footer_company = self.driver.find_element_by_xpath('//*[@id="quick_links"]/a[2]')
        self.footer_career = self.driver.find_element_by_xpath('//*[@id="quick_links"]/a[3]')
        self.footer_faq = self.driver.find_element_by_xpath('//*[@id="quick_links"]/a[4]')
        self.footer_contact = self.driver.find_element_by_xpath('//*[@id="quick_links"]/a[5]')

    def present(self) -> bool:
        for element in (
                self.footer_career, self.footer_company, self.footer_contact, self.footer_faq, self.footer_whyus):
            if not element.is_displayed():
                return False

        return True


class PageUrl:
    def general_url(self):
        url = "http://console.sonikpass.com/"
        return url



