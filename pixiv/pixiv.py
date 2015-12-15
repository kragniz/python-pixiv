from abc import ABCMeta, abstractmethod
import json

import requests
import six


class Authed(object):
    '''Base class for classes that need to make authenticated calls.'''

    def __init__(self, auth_token=None):
        self.auth_token = auth_token

    def get(self, url, params={}):
        headers = {'Authorization': 'Bearer {}'.format(self.auth_token)}
        return requests.get(url, params=params, headers=headers)


@six.add_metaclass(ABCMeta)
class BaseUser(object):
    @abstractmethod
    def works(self):
        '''Return works for this user'''
        pass


class User(BaseUser, Authed):
    '''A Pixiv user'''

    def __init__(self, id, auth_token=None):
        super(User, self).__init__(auth_token=auth_token)
        self.id = id

    def works(self):
        params = {
            'page': 1,
            'per_page': 30,
            'include_stats': True,
            'include_sanity_level': True,
            'image_sizes': ','.join(['px_128x128', 'px_480mw', 'large'])
        }
        return self.get('https://public-api.secure.pixiv.net'
                        '/v1/users/{}/works.json'.format(self.id),
                        params=params)


class Pixiv(Authed):
    '''Store session data'''

    def __init__(self):
        self.auth_token = None

    def login(self, username, password):
        '''Logs the user into Pixiv.

        :param str username: login name
        :param str password: password for the login
        '''

        url = 'https://oauth.secure.pixiv.net/auth/token'

        data = {
            'client_id': 'bYGKuGVw91e0NMfPGp44euvGt59s',
            'client_secret': 'HP3RmkgAmEGro0gn1x9ioawQE8WMfvLXDz3ZqxpK',
            'grant_type': 'password',
            'username': username,
            'password': password
        }

        resp = requests.post(url, data=data)

        if resp.status_code != 200:
            raise Exception('Failed to auth')

        blob = json.loads(resp.text)
        self.auth_token = blob.get('response').get('access_token')

    def user(self, user_id):
        '''Return a :class:`.User` object for a particular Pixiv user.

        :param int user_id: ID of the user
        '''

        return User(user_id, auth_token=self.auth_token)
