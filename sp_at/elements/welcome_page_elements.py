class WelcomePageElements:
    def __init__(self, driver):
        self.driver = driver

    def welcome_time(self):
        return self.driver.find_element_by_xpath('//*[@id="content_leftX"]/h1')

    def content_block(self):
        return self.driver.find_element_by_id('welcome-cta')

    def dashboard_button(self):
        return self.driver.find_element_by_xpath('//*[@id="welcome-cta"]/p[2]/a[1]/button')

    def partner_button(self):
        return self.driver.find_element_by_xpath('//*[@id="welcome-cta"]/p[2]/a[2]/button')

    def logout_button(self):
        return self.driver.find_element_by_xpath('//*[@id="app-container"]/div[2]/button')
