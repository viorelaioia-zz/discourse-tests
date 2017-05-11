from selenium.webdriver.common.by import By

from pages.base import Base
from pages.home_page import Home


class Register(Base):
    _username_locator = (By.ID, 'new-account-username')
    _name_locator = (By.ID, 'new-account-name')
    _create_new_account_button_locator = (By.CSS_SELECTOR, '.modal-footer .btn-primary')

    def enter_username(self, username):
        self.selenium.find_element(*self._username_locator).clear()
        self.selenium.find_element(*self._username_locator).send_keys(username)

    def click_create_new_account_button(self):
        self.selenium.find_element(*self._create_new_account_button_locator).click()
        return Home(self.base_url, self.selenium)
