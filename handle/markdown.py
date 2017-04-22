# _*_ coding: utf-8 _*_

from markdown import markdown
from bleach import clean


def md2html(*args, cleaned=True):
    if cleaned:
        return markdown(clean(args))
    else:
        return markdown(args)
