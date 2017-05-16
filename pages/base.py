from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.auth0 import Auth0
from pages.page import Page
from tests import conftest


class Base(Page):
    _login_button_locator = (By.CSS_SELECTOR, 'button.login-button')
    _avatar_image_locator = (By.CSS_SELECTOR, '#current-user a[class="icon"]')
    _logout_button_locator = (By.CSS_SELECTOR, '.widget-link.logout')
    _page_not_found_error_message_locator = (By.CSS_SELECTOR, '.page-not-found')
    _subcategory_locator = (By.CSS_SELECTOR, '.category-navigation .category-breadcrumb li:nth-child(2) a[aria-label="Display category list"]')
    _preferences_button_locator = (By.CSS_SELECTOR, '.user-preferences-link')

    @property
    def page_title(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.title)
        return self.selenium.title

    @property
    def is_login_button_displayed(self):
        return self.is_element_visible(*self._login_button_locator)

    @property
    def is_avatar_displayed(self):
        return self.is_element_visible(*self._avatar_image_locator)

    @property
    def page_not_found_error_message(self):
        self.wait_for_element_visible(*self._page_not_found_error_message_locator)
        return self.selenium.find_element(*self._page_not_found_error_message_locator).text

    @property
    def subcategory(self):
        return self.selenium.find_element(*self._subcategory_locator).text

    def click_sign_in_button(self):
        self.selenium.find_element(*self._login_button_locator).click()

    def login(self, email):
        self.click_sign_in_button()
        auth0 = Auth0(self.base_url, self.selenium)
        auth0.request_login_link(email)
        login_link = conftest.login_link(email)
        self.selenium.get(login_link)

    def click_avatar(self):
        self.selenium.find_element(*self._avatar_image_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.selenium.find_element(*self._logout_button_locator))

    def click_logout_menu_item(self):
        self.click_avatar()
        self.selenium.find_element(*self._logout_button_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_login_button_displayed)

    def click_preferences(self):
        self.selenium.find_element(*self._preferences_button_locator).click()
        from pages.account import Account
        return Account(self.base_url, self.selenium)

    def create_new_user(self, email):
        self.login(email)
        from pages.register import Register
        return Register(self.base_url, self.selenium)
