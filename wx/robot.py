from  werobot import WeRoBot
from wx.wx_config import CONFIG

robot = WeRoBot(config=CONFIG)


@robot.handler
def hello(message):
    return 'Hello World!'
