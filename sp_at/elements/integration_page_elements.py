class IntegrationPageElements:
    def __init__(self, driver):
        self.driver = driver

    def integration_title(self):
        return self.driver.find_element_by_xpath('//*[@id="content_left"]/h1')

    def what_next_block(self):
        return self.driver.find_element_by_id('content_right')

    def schedule_block(self):
        return self.driver.find_element_by_id('content_left')

    def schedule_button(self):
        return self.driver.find_element_by_xpath('//*[@id="content_right"]/a/button')
