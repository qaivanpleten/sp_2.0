import unittest, pytest
from selenium import webdriver


class SetUpClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome() #"C:\\Users\Владелец\PycharmProjects\chromedriver"
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://console.stage.sonikpass.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main(verbosity=2)
