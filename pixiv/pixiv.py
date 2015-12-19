from abc import ABCMeta, abstractmethod
import json

import requests
import six

from . import utils


class Authed(object):
    '''Base class for classes that need to make authenticated calls.'''

    def __init__(self, auth_token=None):
        self.auth_token = auth_token

    def get(self, url, params={}):
        headers = {'Authorization': 'Bearer {}'.format(self.auth_token)}
        return requests.get(url, params=params, headers=headers)


class Work(Authed):
    '''A Pixiv artwork

    :param int id: the id of this work
    '''

    def __init__(self, id, auth_token=None):
        super(Work, self).__init__(auth_token=auth_token)
        self.id = id
        self.image = None
        self.title = None
        self.width = None
        self.height = None
        self.tags = []

    def __str__(self):
        return 'Work: {title} ({width}x{height})'.format(
            title=self.title,
            width=self.width,
            height=self.height)

    def _load_data(self, api_data):
        image_urls = api_data.get('image_urls')
        self.image = image_urls.get('large')
        utils.copy_dict_items_to_object(self, api_data, ('title',
                                                         'width',
                                                         'height',
                                                         'tags',))

    @classmethod
    def from_api_data(cls, api_data):
        '''Return a new instance populated with data from the API'''
        work = cls(api_data.get('id'))
        work._load_data(api_data)
        return work

    @property
    def link(self):
        return ('http://www.pixiv.net/member_illust.php?'
                'illust_id={id}&mode=medium'.format(id=self.id))


@six.add_metaclass(ABCMeta)
class BaseUser(object):
    @abstractmethod
    def works(self):
        '''Return works for this user'''
        pass


class User(BaseUser, Authed):
    '''A Pixiv user

    :param int id: the id of this user
    '''

    def __init__(self, id, auth_token=None):
        super(User, self).__init__(auth_token=auth_token)
        self.id = id

    def works(self):
        '''Return a list of :class:`.Work` created by this user'''

        # FIXME: this does not handle pagination
        params = {
            'page': 1,
            'per_page': 30,
            'include_stats': True,
            'include_sanity_level': True,
            'image_sizes': ','.join(['px_128x128', 'px_480mw', 'large'])
        }
        api_data = self.get('https://public-api.secure.pixiv.net'
                            '/v1/users/{}/works.json'.format(self.id),
                            params=params)
        api_data_dict = json.loads(api_data.text)
        works_data = api_data_dict.get('response')

        return [Work.from_api_data(d) for d in works_data]


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
        :rtype: :class:`.User`
        '''

        return User(user_id, auth_token=self.auth_token)

    def work(self, work_id):
        '''Return a :class:`.Work` object with a specified ID.

        :param int work_id: ID of the artwork
        :rtype: :class:`.Work`
        '''

        return Work(work_id, auth_token=self.auth_token)

    def search(self, terms, period='all', order='asc'):
        '''Search pixiv and return a list of :class:`.Work` objects.

        :param str terms: search terms
        :param str period: period to search over. This must be one of
                           ``'all'``, ``'day'``, ``'week'`` or ``'month'``
        :param str order: sort order to list results. This must be either
                          ``'asc'`` or ``'desc'``
        '''

        url = 'https://public-api.secure.pixiv.net/v1/search/works.json'

        params = {
            'q': terms,
            'period': period,
            'order': order,
            'mode': 'caption',
            'sort': 'date',
            'image_sizes': ','.join(['px_128x128', 'px_480mw', 'large'])
        }
        resp = self.get(url, params=params)
        api_data_dict = json.loads(resp.text)
        print(api_data_dict)
        works_data = api_data_dict.get('response')

        return [Work.from_api_data(d) for d in works_data]
