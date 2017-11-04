class WhyPageElements:
    def __init__(self, driver):
        self.driver = driver

    def why_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span/p[1]')

    def ten_reasons_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span/h1')

    def ten_reasons_text_block(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span/ol')

    def have_question_button(self):
        return self.driver.find_element_by_class_name('transparent-btn')

    def try_it_button(self):
        return self.driver.find_element_by_class_name('gradient-btn')
