from __future__ import print_function

__author__ = 'Louis Taylor'
__email__ = 'louis@kragniz.eu'
__version__ = '0.1.1'

from .pixiv import Pixiv
from .pixiv import User
from .pixiv import Work


def login(username, password, session=None):
    p = Pixiv(session=session)
    p.login(username, password)
    return p

__all__ = (
    'login',
    'Pixiv',
    'User',
    'Work',
)
