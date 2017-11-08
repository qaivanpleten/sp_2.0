from selenium.webdriver.remote.webdriver import WebDriver

from sp_at.pages.general_element import PageUrl


class AboutUsPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get(PageUrl().general_url() + "#about")

    def check_url(self) -> bool:
        if self._driver.current_url == (PageUrl().general_url() + "#about"):
            return True


class MeetTheTeamBlock:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def team(self) -> iter:
        for xpath_selector in range(3, 8):
            yield self._driver.find_element_by_xpath(
                '//*[@id="sub-region"]/div/section/div[' + str(xpath_selector) + ']')

    def present(self) -> bool:
        for member in self.team():
            if not member.is_displayed():
                return False

        return True


class Body:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._title = self._driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[1]/div/h1')
        self._meet_the_team_title = self._driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[2]/div/h1')
        self.open_positions_button = self._driver.find_element_by_xpath(
            '//*[@id="sub-region"]/div/section/div[8]/div/p/a[1]/button')
        self._get_in_touch_button = self._driver.find_element_by_xpath(
            '//*[@id="sub-region"]/div/section/div[8]/div/p/a[2]/button')

    def present(self) -> bool:
        for element in (self._title, self._meet_the_team_title, self.open_positions_button,
                        self._get_in_touch_button):
            if not element.is_displayed():
                return False

        return True

        # def meet_the_team(self) -> iter:
        #     for xpath_selector in range(3, 8):
        #         yield self.driver.find_element_by_xpath(
        #             '//*[@id="sub-region"]/div/section/div[' + str(xpath_selector) + ']')
        #
        # def meet_the_team_block_present(self) -> bool:
        #     for member in self.meet_the_team():
        #         if not member.is_displayed():
        #             return False
        #
        #     return True


class Button:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open_positions(self):
        return Body(self._driver).open_positions_button

