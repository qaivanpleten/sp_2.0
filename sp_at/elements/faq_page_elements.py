class FaqPageElements:
    def __init__(self, driver):
        self.driver = driver

    def faq_page_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/h1')

    def technology_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/h2[1]')

    def technology_text_block(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/ul[1]')

    def troubleshooting_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/h2[2]')

    def troubleshooting_text_block(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/ul[2]')

    def have_question_button(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/p[2]/a[1]/button')

    def try_it_now_button(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/p[2]/a[2]/button')
