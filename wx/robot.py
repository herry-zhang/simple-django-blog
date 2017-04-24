from django.shortcuts import Http404
from  werobot import WeRoBot
from wx.wx_config import ENCODING_AES_KEY, TOKEN, APP_ID, APP_SECRET, SESSION_STORAGE

robot = WeRoBot(
    token=TOKEN,
    app_id=APP_ID,
    app_secret=APP_SECRET,
    encoding_aes_key=ENCODING_AES_KEY,
    enable_session=SESSION_STORAGE,
)


@robot.handler
def hello(message):
    return 'Hello World!'


@robot.error_page
def make_error_page(url):
    raise Http404
