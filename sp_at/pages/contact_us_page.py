from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.pages.general_element import PageUrl


class ContactUsPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(PageUrl().general_url() + '#contact')

    def check_url(self) -> bool:
        if self._driver.current_url == (PageUrl().general_url() + '#contact'):
            return True


class Body:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._title = self._driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/h1')
        self._partnership_email = self._driver.find_element_by_xpath(
            '//*[@id="sub-region"]/div/section/div/div/p[1]/a[1]')
        self._support_email = self._driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[1]/a[2]')
        self._sales_email = self._driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[1]/a[3]')
        self._general_email = self._driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[1]/a[2]')
        self._faq_button = self._driver.find_element_by_xpath(
            '//*[@id="sub-region"]/div/section/div/div/p[2]/a[1]/button')
        self._try_it_now_button = self._driver.find_element_by_xpath(
            '//*[@id="sub-region"]/div/section/div/div/p[2]/a[2]/button')

    def present(self) -> bool:
        for element in (self._title, self._partnership_email, self._support_email, self._sales_email,
                        self._general_email, self._faq_button, self._try_it_now_button):
            if not element.is_displayed():
                return False

        return True


class Button:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._faq_button = self._driver.find_element_by_xpath(
            '//*[@id="sub-region"]/div/section/div/div/p[2]/a[1]/button')
        self._try_it_now_button = self._driver.find_element_by_xpath(
            '//*[@id="sub-region"]/div/section/div/div/p[2]/a[2]/button')

    def faq(self):
        return self._faq_button

    def try_it_now(self):
        return self._try_it_now_button
