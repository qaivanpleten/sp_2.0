class InstallPageElements:
    def __init__(self, driver):
        self.driver = driver

    def install_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/h1')

    def install_on_ios(self):
        return self.driver.find_element_by_id('download-ios')

    def install_desktop(self):
        return self.driver.find_element_by_id('download-osx')

    def install_on_android(self):
        return self.driver.find_element_by_id('download-android')

    def content_block(self):
        return self.driver.find_element_by_class_name('content')

    def troubleshooting_title(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/div/h3[2]')

    def troubleshooting_block(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/div/ul')

    def troubleshooting_button_how_do_(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/div/ul/li[1]/div/a/span[2]')

    def troubleshooting_text_how_do_(self):
        return self.driver.find_element_by_id('answer-1')

    def troubleshooting_button_app_is(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/div/ul/li[2]/div/a/span[2]')

    def troubleshooting_text_app_is(self):
        return self.driver.find_element_by_id('answer-2')

    def troubleshooting_button_download(self):
        return self.driver.find_element_by_xpath('//*[@id="flex_center"]/div/ul/li[3]/div/a/span[2]')

    def troubleshooting_text_download(self):
        return self.driver.find_element_by_id('answer-3')
