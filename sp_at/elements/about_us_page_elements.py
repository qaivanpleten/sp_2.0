class AboutPageElements:
    def __init__(self, driver):
        self.driver = driver

    def about_title(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[1]/div/h1')

    def meet_the_team_title(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[2]/div/h1')

    def portfolio_block(self, xpath_selector):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[' + xpath_selector + ']')

    def open_positions_button(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[8]/div/p/a[1]/button')

    def get_in_touch_button(self):
        return self.driver.find_element_by_xpath('//*[@id="sub-region"]/div/section/div[8]/div/p/a[2]/button')
