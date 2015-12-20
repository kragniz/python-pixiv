class PixivError(Exception):
    '''Base pixiv error'''


class NotAuthedError(PixivError):
    '''Exception class for when you haven't authed yet'''
