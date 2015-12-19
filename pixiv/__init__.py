from __future__ import print_function

__author__ = 'Louis Taylor'
__email__ = 'louis@kragniz.eu'
__version__ = '0.1.0'

from .pixiv import Pixiv
from .pixiv import User


def login(username, password):
    p = Pixiv()
    p.login(username, password)
    return p

__all__ = (
    'Pixiv',
    'User',
    'Work',
)
