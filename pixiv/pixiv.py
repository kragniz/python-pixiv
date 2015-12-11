import json

import requests


class Authed(object):
    def __init__(self, auth_token=None):
        self.auth_token = auth_token

    def get(self, url, params={}):
        headers = {'Authorization': 'Bearer {}'.format(self.auth_token)}
        return requests.get(url, params=params, headers=headers)


class User(Authed):
    def __init__(self, user_id, auth_token=None):
        super(User, self).__init__(auth_token=auth_token)
        self.user_id = user_id

    def works(self):
        params = {
            'page': 1,
            'per_page': 30,
            'include_stats': True,
            'include_sanity_level': True,
            'image_sizes': ','.join(['px_128x128', 'px_480mw', 'large'])
        }
        return self.get('https://public-api.secure.pixiv.net'
                        '/v1/users/{}/works.json'.format(self.user_id),
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
        return User(user_id, auth_token=self.auth_token)
