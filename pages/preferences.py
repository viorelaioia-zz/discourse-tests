from selenium.webdriver.common.by import By

from pages.base import Base
from pages.page import PageRegion


class Preferences(Base):
    _account_button_locator = (By.CSS_SELECTOR, 'li[class*="nav-account"] a')
    _categories_button_locator = (By.CSS_SELECTOR, 'li[class*="no-glyph indent nav-categories"] a')
    _user_preferences_section_locator = (By.CSS_SELECTOR, '.user-right.user-preferences')

    @property
    def account(self):
        self.selenium.find_element(*self._account_button_locator).click()
        return self.Account(self.base_url, self.selenium,
                            self.selenium.find_element(*self._user_preferences_section_locator))

    @property
    def categories(self):
        self.selenium.find_element(*self._categories_button_locator).click()
        return self.Category(self.base_url, self.selenium,
                             self.selenium.find_element(*self._user_preferences_section_locator))

    class Account(PageRegion):
        _delete_account_button_locator = (By.CSS_SELECTOR, '.delete-account button')
        _delete_account_confirmation_locator = (By.CSS_SELECTOR, '.modal-footer .btn-danger')

        def delete_account(self):
            self.selenium.find_element(*self._delete_account_button_locator).click()
            self.wait_for_element_visible(*self._delete_account_confirmation_locator)
            self.selenium.find_element(*self._delete_account_confirmation_locator).click()
            from pages.home_page import Home
            return Home(self.base_url, self.selenium)

    class Category(PageRegion):
        _watched_categories_locator = (By.CSS_SELECTOR, 'div[class*="category-controls"]:first-of-type div[class="item"]')
        _delete_category_buttons_locator = (By.CSS_SELECTOR, 'div[class*="category-controls"]:first-of-type a[class="remove"]')
        _save_button_locator = (By.CSS_SELECTOR, 'button[class*="save-user"]')

        @property
        def watched_categories(self):
            watched_categories = self.selenium.find_elements(*self._watched_categories_locator)
            return [category.text for category in watched_categories]

        def remove_category(self, category):
            category_index = self.watched_categories.index(category)
            delete_watched_categories_buttons = self.selenium.find_elements(*self._delete_category_buttons_locator)
            delete_watched_categories_buttons[category_index].click()

        def click_save_button(self):
            self.selenium.find_element(*self._save_button_locator).click()
