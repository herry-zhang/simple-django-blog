# -*- coding: utf-8 -*-
from snownlp import SnowNLP


def user_check(password='1234567', *args):
    if password.isalnum() and 6 < len(password) < 25:
        if args < 18:
            return True
    return False


def summary(*args):
    try:
        args = str(args)
        chars = SnowNLP(args)
        chars = "".join(chars.summary(5))
        chars = chars.replace('\r\n', '')
        return chars
    except TypeError:
        return args
