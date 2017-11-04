class ContactPageElements:
    def __init__(self, driver):
        self.driver = driver

    def contact_title(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/h1')

    def partnership_email(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[1]/a[1]')

    def support_email(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[1]/a[2]')

    def sales_email(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[1]/a[3]')

    def general_email(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[1]/a[2]')

    def faq_button(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[2]/a[1]/button')

    def try_it_button(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div/div/p[2]/a[2]/button')
