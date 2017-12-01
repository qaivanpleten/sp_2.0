import time

from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.pages.general_element import PageUrl


class InstallPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(PageUrl().general_url() + '#install')

    def check_sonicpass_url(self):
        if self._driver.current_url == PageUrl().general_url() + '#install':
            return True

    def check_url(self, url):
        if self._driver.current_url == url:
            return True


class Body:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._content_block = self._driver.find_element_by_id('flex_center')
        self._install_title = self._driver.find_element_by_xpath('//*[@id="flex_center"]/h1')
        self._troubleshooting_title = self._driver.find_element_by_xpath('//*[@id="flex_center"]/div/h3[2]')
        self._troubleshooting_block = self._driver.find_element_by_xpath('//*[@id="flex_center"]/div/ul')
        self._troubleshooting_button_how_do = self._driver.find_element_by_xpath(
            '//*[@id="flex_center"]/div/ul/li[1]/div/a/span[2]')
        self._troubleshooting_text_how_do = self._driver.find_element_by_id('answer-1')
        self._troubleshooting_button_app_is = self._driver.find_element_by_xpath(
            '//*[@id="flex_center"]/div/ul/li[2]/div/a/span[2]')
        self._troubleshooting_text_app_is = self._driver.find_element_by_id('answer-2')
        self._troubleshooting_button_download = self._driver.find_element_by_xpath(
            '//*[@id="flex_center"]/div/ul/li[3]/div/a/span[2]')
        self._troubleshooting_text_download = self._driver.find_element_by_id('answer-3')

    def present(self) -> bool:
        for element in (self._content_block, self._install_title, self._troubleshooting_title,
                        self._troubleshooting_block, self._troubleshooting_button_how_do,
                        self._troubleshooting_button_app_is, self._troubleshooting_button_download):
            if not element.is_displayed():
                return False

        self._troubleshooting_button_how_do.click()
        time.sleep(1)

        if not self._troubleshooting_text_how_do.is_displayed():
            return False
        time.sleep(1)

        self._troubleshooting_button_app_is.click()
        time.sleep(1)

        if not self._troubleshooting_text_app_is.is_displayed():
            return False
        time.sleep(1)

        self._troubleshooting_button_download.click()
        time.sleep(1)

        if not self._troubleshooting_text_download.is_displayed():
            return False
        time.sleep(1)

        return True



