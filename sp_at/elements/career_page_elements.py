class CareerPageElements:
    def __init__(self, driver):
        self.driver = driver

    def career_title(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/h1')

    def career_text(self, xpath_locator):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[' + xpath_locator + ']')

    def faq_button(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[6]/a[1]/button')
