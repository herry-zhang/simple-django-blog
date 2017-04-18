# _*_ coding: utf-8 _*_

from PIL import Image
from hashlib import sha256
from random import choice, sample
from string import digits, ascii_letters


# "(chars)".join(random.sample(digits+ascii_letters, 8))
def random_char(length=8, pre=''):
    return pre.join(choice(digits + ascii_letters for _ in range(length)))


def jpg_hash(text):
    return '{0}.jpg'.format(sha256(text.encode('utf-8')).hexdigest())


def thumbnail(pic, size=(100, 100)):
    with Image.open(pic) as im:
        im = im.convert('RGB')
        im = im.thumbnail(size)
    return im

def addphoto(request, name='photo'):
    f = request.FILES[name]
