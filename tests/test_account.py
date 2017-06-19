# coding=utf-8
import random
import uuid

import pytest

from pages.home_page import Home
from tests import conftest


class TestAccount:

    @pytest.mark.nondestructive
    def test_login_logout(self, base_url, selenium, unvouched_user):
        home_page = Home(base_url, selenium)
        home_page.login(unvouched_user['email'])
        assert home_page.is_avatar_displayed
        home_page.click_logout_menu_item()
        assert home_page.is_login_button_displayed

    @pytest.mark.nondestructive
    def test_unvouched_mozillian_cannot_access_private_categories(self, base_url, selenium, unvouched_user):
        home_page = Home(base_url, selenium)
        home_page.login(unvouched_user['email'])
        assert home_page.is_avatar_displayed
        home_page.go_to_url('https://discourse.mozilla-community.org/c/mozillians/vouched-mozillians')
        error_message = 'Oops! That page doesn’t exist or is private.'.decode('utf8')
        assert error_message == home_page.page_not_found_error_message
        home_page.go_to_url('https://discourse.mozilla-community.org/c/mozillians/nda')
        assert error_message == home_page.page_not_found_error_message

    @pytest.mark.nondestructive
    def test_vouched_mozillian_can_access_private_category(self, base_url, selenium, vouched_user):
        home_page = Home(base_url, selenium)
        home_page.login(vouched_user['email'])
        assert home_page.is_avatar_displayed
        home_page.go_to_url('https://discourse.mozilla-community.org/c/mozillians/vouched-mozillians')
        assert 'Vouched Mozillians' == home_page.subcategory
        home_page.click_logout_menu_item()

    @pytest.mark.nondestructive
    def test_create_and_delete_account(self, base_url, selenium, new_user):
        home_page = Home(base_url, selenium)
        register = home_page.create_new_user(new_user['email'])
        register.enter_username("test_user")
        home_page = register.click_create_new_account_button()
        assert home_page.is_avatar_displayed
        preferences = home_page.click_preferences()
        home_page = preferences.account.delete_account()
        assert home_page.is_login_button_displayed

    @pytest.mark.nondestructive
    def test_user_can_watch_category(self, base_url, selenium, unvouched_user):
        home_page = Home(base_url, selenium)
        home_page.login(unvouched_user['email'])
        assert home_page.is_avatar_displayed
        home_page.click_toggle_menu()
        categories = home_page.categories_list_names
        category = random.choice(categories)
        category_page = home_page.select_category(category)
        category_page.click_notifications_dropdown()
        category_page.select_option("Watching")
        preferences = category_page.click_preferences()
        preferences_category_page = preferences.categories
        assert category in preferences_category_page.watched_categories
        preferences_category_page.remove_category(category)
        preferences_category_page.click_save_button()
        preferences.click_logout_menu_item()
        assert home_page.is_login_button_displayed

    @pytest.mark.nondestructive
    def test_user_can_go_through_existing_categories(self, base_url, selenium, vouched_user):
        home_page = Home(base_url, selenium)
        home_page.login(vouched_user['email'])
        assert home_page.is_avatar_displayed
        home_page.click_toggle_menu()
        categories_list = home_page.categories_list_names
        for category_name in categories_list:
            index = categories_list.index(category_name)
            home_page.select_category(categories_list[index])
            assert home_page.category == category_name
            home_page.click_toggle_menu()
        home_page.click_logout_menu_item()

    @pytest.mark.nondestructive
    def test_user_can_create_a_new_topic(self, base_url, selenium, ldap_user):
        home_page = Home(base_url, selenium)
        home_page.login_with_ldap(ldap_user['email'], ldap_user['password'], conftest.passcode(ldap_user['secret_seed']))
        assert home_page.is_avatar_displayed
        home_page.click_add_new_topic()
        title = "Test topic - {0}".format(uuid.uuid1())
        home_page.enter_new_topic_title(title)
        category = "playground"
        home_page.select_category(category)
        description = "This is a topic description for testing - {}".format(uuid.uuid1())
        home_page.enter_topic_description(description)
        topic_page = home_page.click_create_topic()
        assert title == topic_page.topic_title
        assert category == topic_page.topic_category
        assert description == topic_page.topic_description
        topic_page.click_logout_menu_item()
        assert topic_page.is_login_button_displayed
