from sp_at.elements.main_page_elements import MainPageElements


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class GeneralActions(BasePage):
    def click_on_button(self, button_locator):
        button_locator.click()

    def check_element_on_page(self, element):
        assert element.is_displayed(), ("Element " + str(element) + "isn't displayed on the page")

    def check_atribute_of_element(self, element, attribute):
        assert 'width: 100%; background-position: 100% 0px;' in (element.get_attribute(attribute))

    def check_active_button_in_sidebar(self, value):
        assert value in MainPageElements(self.driver).sidebar().get_attribute('style')

    def scroll_page(self, value):
        self.driver.execute_script("window.scrollTo(0, " + value + ")")

    def check_url(self, link):
        assert link in self.driver.current_url

    def open_page_by_url(self, url):
        self.driver.get(url)
