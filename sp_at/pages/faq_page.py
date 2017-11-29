from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.pages.general_element import PageUrl


class FaqPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(PageUrl().general_url() + '#faq')

    def check_url(self):
        if self._driver.current_url == (PageUrl().general_url() + '#faq'):
            return True


class Body:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._faq_page_title = self._driver.find_element_by_xpath('//*[@id="flex_center"]/h1')
        self._technology_title = self._driver.find_element_by_xpath('//*[@id="flex_center"]/h2[1]')
        self._technology_text_block = self._driver.find_element_by_xpath('//*[@id="flex_center"]/ul[1]')
        self._troubleshooting_title = self._driver.find_element_by_xpath('//*[@id="flex_center"]/h2[2]')
        self._troubleshooting_text_block = self._driver.find_element_by_xpath('//*[@id="flex_center"]/ul[2]')
        self._question_button = self._driver.find_element_by_xpath('//*[@id="flex_center"]/p[2]/a[1]/button')
        self._try_it_now = self._driver.find_element_by_xpath('//*[@id="flex_center"]/p[2]/a[2]/button')

    def present(self) -> bool:
        for element in (self._faq_page_title, self._technology_title, self._technology_text_block,
                        self._troubleshooting_title, self._technology_text_block, self._question_button,
                        self._try_it_now):
            if not element.is_displayed():
                return False

        return True


class Button:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._try_it_now = self._driver.find_element_by_xpath('//*[@id="flex_center"]/p[2]/a[2]/button')

    def try_it_now(self):
        return self._try_it_now
