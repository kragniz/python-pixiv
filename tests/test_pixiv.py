'''Tests for `pixiv` module.'''

import unittest

import betamax
import pytest
import requests

import pixiv

pytest.mark.usefixtures('betamax_session')

test_username = 'username'
test_password = 'password'

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'tests/cassettes'
    config.define_cassette_placeholder('pixiv-password', test_password)
    config.define_cassette_placeholder('pixiv-username', test_username)


class TestPixiv:
    def test_login(self, betamax_session):
        p = pixiv.Pixiv(session=betamax_session)
        p.login(test_username, test_password)
