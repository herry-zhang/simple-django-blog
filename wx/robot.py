import re
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


@robot.subscribe
def subscribe(message):
    return '欢迎关注，回复“博客”或者“1”打开博客'


@robot.filter(re.compile("^((博客)|1)$"))
def blog(session):
    if "ask_blog_times" in session:
        session['ask_blog_times'] += 1
    session["ask_blog_times"] = 1
    return "http://www.willtunner.me"


@robot.error_page
def make_error_page(url):
    raise Http404
