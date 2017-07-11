from selenium.webdriver.common.by import By

from pages.page import Page


class Auth0(Page):

    _login_with_email_button_locator = (By.CSS_SELECTOR, '.auth0-lock-passwordless-button.auth0-lock-passwordless-big-button')
    _email_input_locator = (By.CSS_SELECTOR, '.auth0-lock-passwordless-pane>div>div>input')
    _send_email_button_locator = (By.CSS_SELECTOR, '.auth0-lock-passwordless-submit')

    _login_with_ldap_button_locator = (By.CSS_SELECTOR, '.auth0-lock-ldap-button.auth0-lock-ldap-big-button')
    _ldap_email_field_locator = (By.CSS_SELECTOR, '.auth0-lock-input-email .auth0-lock-input')
    _ldap_password_field_locator = (By.CSS_SELECTOR, '.auth0-lock-input-password .auth0-lock-input')
    _login_button_locator = (By.CSS_SELECTOR, '.auth0-lock-submit')

    _enter_passcode_button = (By.CSS_SELECTOR, '.passcode-label .positive.auth-button')
    _passcode_field_locator = (By.CSS_SELECTOR, '.passcode-label input[name="passcode"]')
    _duo_iframe_locator = (By.ID, 'duo_iframe')

    def request_login_link(self, username):
        self.wait_for_element_visible(*self._login_with_email_button_locator)
        self.selenium.find_element(*self._login_with_email_button_locator).click()
        self.wait_for_element_visible(*self._email_input_locator)
        self.selenium.find_element(*self._email_input_locator).send_keys(username)
        self.selenium.find_element(*self._send_email_button_locator).click()

    def login_with_ldap(self, email, password, passcode):
        self.wait_for_element_visible(*self._login_with_ldap_button_locator)
        self.selenium.find_element(*self._login_with_ldap_button_locator).click()
        self.selenium.find_element(*self._ldap_email_field_locator).send_keys(email)
        self.selenium.find_element(*self._ldap_password_field_locator).send_keys(password)
        self.selenium.find_element(*self._login_button_locator).click()
        self.enter_passcode(passcode)

    def enter_passcode(self, passcode):
        self.selenium.switch_to_frame('duo_iframe')
        self.wait_for_element_visible(*self._enter_passcode_button)
        self.selenium.find_element(*self._enter_passcode_button).click()
        self.selenium.find_element(*self._passcode_field_locator).send_keys(passcode)
        self.selenium.find_element(*self._enter_passcode_button).click()
        self.selenium.switch_to_default_content()
