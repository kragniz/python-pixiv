import requests


class Pixiv(object):
    def __init__(self):
        pass

    def login(self, username, password):
        url = 'https://oauth.secure.pixiv.net/auth/token'

        data = {
            'client_id': 'bYGKuGVw91e0NMfPGp44euvGt59s',
            'client_secret': 'HP3RmkgAmEGro0gn1x9ioawQE8WMfvLXDz3ZqxpK',
            'grant_type': 'password',
            'username': username,
            'password': password
        }

        resp = requests.post(url, data=data)
        print(resp.status_code, resp.text)
