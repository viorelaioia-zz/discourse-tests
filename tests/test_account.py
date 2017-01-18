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
