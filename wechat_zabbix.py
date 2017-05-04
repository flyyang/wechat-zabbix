import sys
from wechat import WeChat

wechat = WeChat()

wechat.send(sys.argv[2], sys.argv[3])
