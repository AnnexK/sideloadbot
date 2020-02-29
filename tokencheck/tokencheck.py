import hashlib


class InvalidTokenError(Exception):
    pass


def check_token(token):
    b = bytes(token, encoding='utf8')
    digest = hashlib.sha256(b).digest()
    return digest == b'\xceML\xc7\x87\xc5\xc1\xe3\xc6&\x98\xd7\xe8\xe5K\xef\xa4\xac,\xa1\xd4V\x98\x11\xca\x8d\xf2#!\xcb\x80\xef'
