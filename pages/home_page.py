from selenium.webdriver.common.by import By

from pages.base import Base
from pages.topic_page import TopicPage


class Home(Base):
    _create_new_topic_button_locator = (By.ID, 'create-topic')
    _new_title_topic_locator = (By.ID, 'reply-title')
    _category_combobox_locator = (By.CSS_SELECTOR, '.category-input div[class*="category-combobox"]')
    _category_input_locator = (By.CSS_SELECTOR, '.select2-search .select2-input')
    _search_results_locator = (By.CSS_SELECTOR, '.select2-results .badge-wrapper.bar')
    _topic_description_locator = (By.CSS_SELECTOR, 'div[class*="textarea-wrapper"] textarea')
    _create_topic_button_locator = (By.CSS_SELECTOR, '.submit-panel button')
    _similar_topics_window_locator = (By.CSS_SELECTOR, '.composer-popup.hidden.similar-topics')
    _close_similar_topics_window_button = (By.CSS_SELECTOR, '.composer-popup.hidden.similar-topics .close')

    def __init__(self, base_url, selenium, open_url=True):
        Base.__init__(self, base_url, selenium)
        if open_url:
            self.selenium.get(self.base_url)

    def click_add_new_topic(self):
        self.selenium.find_element(*self._create_new_topic_button_locator).click()

    def enter_new_topic_title(self, title):
        self.wait_for_element_visible(*self._new_title_topic_locator)
        self.selenium.find_element(*self._new_title_topic_locator).send_keys(title)

    def select_category(self, category):
        self.selenium.find_element(*self._category_combobox_locator).click()
        self.wait_for_element_visible(*self._category_input_locator)
        self.selenium.find_element(*self._category_input_locator).send_keys(category)
        search_results = self.selenium.find_elements(*self._search_results_locator)
        for item in search_results:
            if item.text == category:
                item.click()

    def enter_topic_description(self, description):
        self.selenium.find_element(*self._topic_description_locator).send_keys(description)
        self.wait_for_element_visible(*self._similar_topics_window_locator)
        self.selenium.find_element(*self._close_similar_topics_window_button).click()

    def click_create_topic(self):
        self.selenium.find_element(*self._create_topic_button_locator).click()
        return TopicPage(self.base_url, self.selenium)
