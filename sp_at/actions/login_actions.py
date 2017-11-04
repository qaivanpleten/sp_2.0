import time

from sp_at.actions.general_actions import GeneralActions
from sp_at.elements.login_page_elements import LoginPageElements
from sp_at.elements.main_page_elements import MainPageElements
from sp_at.elements.welcome_page_elements import WelcomePageElements


class LoginActions:
    def __init__(self, driver):
        self.driver = driver

    def login_full_case(self, email):
        main_elements = MainPageElements(self.driver)
        login_elements = LoginPageElements(self.driver)
        general_action = GeneralActions(self.driver)

        general_action.click_on_button(main_elements.login_button())
        main_elements.dialog_username_input().click()
        main_elements.dialog_username_input().send_keys(email)
        main_elements.dialog_next_button().click()

        login_elements.use_automatic_button().click()
        login_elements.login_button().click()
        time.sleep(35)

    def login_cancel(self, email):
        main_elements = MainPageElements(self.driver)
        general_action = GeneralActions(self.driver)

        general_action.click_on_button(main_elements.login_button())
        main_elements.dialog_username_input().click()
        main_elements.dialog_username_input().send_keys(email)
        main_elements.dialog_cancel_button().click()

    def logout(self):
        GeneralActions(self.driver).click_on_button(WelcomePageElements(self.driver).logout_button())
