from  werobot import WeRoBot
from wx.wx_config import TOKEN, CONFIG

robot = WeRoBot(config=CONFIG, token=TOKEN)


@robot.handler
def hello(message):
    return 'Hello World!'
