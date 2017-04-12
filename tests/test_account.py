# coding=utf-8
import pytest

from pages.home_page import Home


class TestAccount:

    @pytest.mark.nondestructive
    def test_login_logout(self, base_url, selenium, unvouched_user):
        home_page = Home(base_url, selenium)
        home_page.login(unvouched_user['email'])
        assert home_page.is_avatar_displayed
        home_page.click_logout_menu_item()
        assert home_page.is_login_button_displayed

    @pytest.mark.nondestructive
    def test_verify_unvouched_mozillian_cannot_access_private_categories(self, base_url, selenium, unvouched_user):
        home_page = Home(base_url, selenium)
        home_page.login(unvouched_user['email'])
        assert home_page.is_avatar_displayed
        home_page.go_to_url("https://discourse.mozilla-community.org/c/mozillians/vouched-mozillians")
        error_message = "Oops! That page doesn’t exist or is private.".decode('utf8')
        assert error_message == home_page.page_not_found_error_message
        home_page.go_to_url("https://discourse.mozilla-community.org/c/mozillians/nda")
        assert error_message == home_page.page_not_found_error_message
