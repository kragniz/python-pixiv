'''Tests for `pixiv` module.'''

import os
import unittest

import betamax
import pytest
import requests

import pixiv

pytest.mark.usefixtures('betamax_session')

# run tests with $ USERNAME=live-username PASSWORD=live-password tox -e py27
test_username = os.environ.get('USERNAME', 'pixiv-username')
test_password = os.environ.get('PASSWORD', 'pixiv-password')

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'tests/cassettes'
    config.define_cassette_placeholder('pixiv-username', test_username)
    config.define_cassette_placeholder('pixiv-password', test_password)


class TestPixiv:
    def test_login(self, betamax_session):
        p = pixiv.Pixiv(session=betamax_session)
        p.login(test_username, test_password)
