from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.pages.general_element import PageUrl


class CareerPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(PageUrl().general_url() + '#careers')

    def check_url(self) -> bool:
        if not self._driver.current_url == (PageUrl().general_url() + '#careers'):
            return False

        return True


class Body:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._career_title = self._driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/h1')
        self._open_position_title = self._driver.find_element_by_xpath(
            '//*[@id="sub-region"]/div/section/div/div/p[4]/strong')
        self.faq_button = self._driver.find_element_by_xpath(
            '//*[@id="sub-region"]/div/section/div/div/p[6]/a[1]/button')

    def present(self) -> bool:
        for element in (self._career_title, self._open_position_title, self.faq_button):
            if not element.is_displayed():
                return False

        return True


class CareerTextBlock:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def text_block(self) -> iter:
        for xpath_selector in range(1, 4):
            yield self._driver.find_element_by_xpath(
                '//*[@id="sub-region"]/div/section/div/div/p[' + str(xpath_selector) + ']')

    def present(self) -> bool:
        for paragraph in self.text_block():
            if not paragraph.is_displayed():
                return False

        return True


class Button:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def faq(self):
        return Body(self._driver).faq_button
