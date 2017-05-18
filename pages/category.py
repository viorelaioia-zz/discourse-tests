from selenium.webdriver.common.by import By

from pages.base import Base


class Category(Base):

    _notifications_dropdown_locator = (By.CSS_SELECTOR, '.dropdown-toggle')
    _notification_options_locator = (By.CSS_SELECTOR, '.dropdown-menu li span[class="title"]')
    _options_locator = (By.CSS_SELECTOR, '.dropdown-menu li a')

    @property
    def options(self):
        options_list = self.selenium.find_elements(*self._notification_options_locator)
        return [option.text for option in options_list]

    def click_notifications_dropdown(self):
        self.selenium.find_element(*self._notifications_dropdown_locator).click()

    def select_option(self, option):
        notification_option_index = self.options.index(option)
        notification_options_list = self.selenium.find_elements(*self._options_locator)
        notification_options_list[notification_option_index].click()
