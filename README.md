# discourse-tests
Automated tests for discourse.mozilla-community.org

How to set up and run Discourse tests locally

This repository contains Selenium tests used to test:
* staging: https://discourse.staging.paas.mozilla.community/
* production: https://discourse.mozilla-community.org/

##You will need to install the following:
#### Git
If you have cloned this project already then you can skip this! GitHub has excellent guides for Windows, Mac OS X, and Linux.

#### Python
Before you will be able to run these tests you will need to have Python 2.6.8+ installed.

##Running tests locally
Some of the tests in discourse-tests require accounts for https://discourse.staging.paas.mozilla.community.  You'll need to create two sets of credentials with varying privilege levels.

1. Create two username and password combinations on https://mozillians.org
2. Make sure one of the accounts is vouched 3 times
3. Create the same Two accounts used in step #1 in https://discourse.staging.paas.mozilla.community
4. Copy discourse-tests/variables.json to a location outside of discourse-tests. Update the 'vouched' and 'unvouched' users in variables.json with those credentials

* [Install Tox](https://tox.readthedocs.io/en/latest/install.html)
* Run PYTEST_ADDOPTS="--variables=/path/to/variables.json" tox
