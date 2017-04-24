from  werobot import WeRoBot
from wx.wx_config import *

robot = WeRoBot(APP_SERCRET=APP_SECRET,
                token = TOKEN,
                APP_ID=APP_ID,
                )


@robot.handler
def hello(message):
    return 'Hello World!'
