class PricingPageElements:
    def __init__(self, driver):
        self.driver = driver

    def pricing_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/h1')

    def text(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/p[1]')

    def contact_button(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/p[3]/a[1]/button')

    def try_button(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/p[3]/a[2]/button')
