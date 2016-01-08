# -*- coding: utf-8 -*-
'''Tests for `pixiv` module.'''

import os
import unittest

import betamax
from betamax_serializers import pretty_json
import pytest
import requests

import pixiv

pytest.mark.usefixtures('betamax_session')

# run tests with $ USERNAME=live-username PASSWORD=live-password tox -e py27
test_username = os.environ.get('USERNAME', 'pixiv-username')
test_password = os.environ.get('PASSWORD', 'pixiv-password')

record_mode = 'none' if os.environ.get('CONTINUOUS_INTEGRATION') else 'once'

betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)
with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'tests/cassettes'
    config.default_cassette_options['record_mode'] = record_mode
    config.default_cassette_options['serialize_with'] = 'prettyjson'
    config.define_cassette_placeholder('pixiv-username', test_username)
    config.define_cassette_placeholder('pixiv-password', test_password)


class TestPixiv:
    def test_login(self, betamax_session):
        p = pixiv.Pixiv(session=betamax_session)
        p.login(test_username, test_password)
        assert p.auth_token is not None

    def test_login_helper_function(self, betamax_session):
        p = pixiv.login(test_username, test_password, session=betamax_session)
        assert p.auth_token is not None

    def test_user(self, betamax_session):
        p = pixiv.Pixiv(session=betamax_session)
        p.login(test_username, test_password)
        user = p.user(7631951)
        assert user.id == 7631951

    def test_user_works(self, betamax_session):
        p = pixiv.Pixiv(session=betamax_session)
        p.login(test_username, test_password)
        user = p.user(7631951)
        work = user.works()[0]
        assert work.title == u'星の語'
        assert work.id == 54032421
