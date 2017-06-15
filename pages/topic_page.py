from selenium.webdriver.common.by import By

from pages.base import Base


class TopicPage(Base):
    _topic_title_locator = (By.CSS_SELECTOR, '.fancy-title')
    _topic_category_locator = (By.CSS_SELECTOR, '.title-wrapper .badge-wrapper.bar')
    _topic_description_locator = (By.CSS_SELECTOR, '.regular.contents p')

    @property
    def topic_title(self):
        return self.selenium.find_element(*self._topic_title_locator).text

    @property
    def topic_category(self):
            return self.selenium.find_element(*self._topic_category_locator).text

    @property
    def topic_description(self):
            return self.selenium.find_element(*self._topic_description_locator).text
