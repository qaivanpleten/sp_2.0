from sp_at.elements.career_page_elements import CareerPageElements


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class CareerPageActions(BasePage):
    def check_list_of_elements(self, range_value_start, range_value_finish):
        for x in range(range_value_start, range_value_finish):
            assert CareerPageElements(self.driver).career_text(str(x)).is_displayed()
