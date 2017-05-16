from selenium.webdriver.common.by import By

from pages.base import Base
from pages.home_page import Home


class Account(Base):
    _delete_account_button_locator = (By.CSS_SELECTOR, '.delete-account button')
    _delete_account_confirmation_locator = (By.CSS_SELECTOR, '.modal-footer .btn-danger')

    def delete_account(self):
        self.selenium.find_element(*self._delete_account_button_locator).click()
        self.wait_for_element_visible(*self._delete_account_confirmation_locator)
        self.selenium.find_element(*self._delete_account_confirmation_locator).click()
        return Home(self.base_url, self.selenium)
