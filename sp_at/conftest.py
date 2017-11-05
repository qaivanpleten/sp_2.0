import pytest
from selenium import webdriver

from sp_at.elements.main_page_elements import MainPageElements


@pytest.fixture
def fixture_webdriver() -> webdriver:
    driver = webdriver.Chrome("C:\\Users\Владелец\PycharmProjects\chromedriver") #"C:\\Users\Владелец\PycharmProjects\chromedriver"
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
