class PrivacyPageElements:
    def __init__(self, driver):
        self.driver = driver

    def privacy_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span[1]/h1')

    def first_paragraph(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span[1]/p[2]')

    def second_paragraph(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span[1]/p[3]')

    def third_paragraph(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span[2]/p[1]')

    def fourth_paragraph(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span[2]/p[2]')

    def fifth_paragraph(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span[2]/p[2]')

    def sixth_paragraph(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span[2]/p[3]')

    def seventh_paragraph(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span[2]/p[4]')

    def eighth_paragraph(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span[2]/p[5]')

    def questions_button(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/span[2]/a/button')
