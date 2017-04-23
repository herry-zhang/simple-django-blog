from  werobot import WeRoBot
from wx.wx_config import TOKEN

robot = WeRoBot(token=TOKEN)


@robot.handler
def hello(message):
    return 'Hello World!'
