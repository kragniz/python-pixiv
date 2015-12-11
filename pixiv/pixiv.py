import json

import requests


class Pixiv(object):
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
