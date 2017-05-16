import uuid

import pytest

import restmail


@pytest.fixture
def capabilities(request, capabilities):
    driver = request.config.getoption('driver')
    if capabilities.get('browserName', driver).lower() == 'firefox':
        capabilities['marionette'] = True
    return capabilities


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


@pytest.fixture
def stored_users(variables):
    return variables['users']


@pytest.fixture
def vouched_user(stored_users):
    return stored_users['vouched']


@pytest.fixture
def unvouched_user(stored_users):
    return stored_users['unvouched']


@pytest.fixture
def new_email():
    return 'test_user_{0}@restmail.net'.format(uuid.uuid1())


@pytest.fixture
def new_user(new_email):
    return {'email': new_email}


@pytest.fixture
def login_link(username):
    mail = restmail.get_mail(username)
    mail_content = mail[0]['text'].replace('\n', ' ').replace('amp;', '').split(" ")
    for link in mail_content:
        if link.startswith("https"):
            return link
