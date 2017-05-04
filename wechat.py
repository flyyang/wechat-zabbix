# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import ast
import json
from config import wechat_conf
class WeChat(object):

    def __init__(self):
        self.corpid = wechat_conf["corpid"]
        self.corpsecret = wechat_conf["corpsecret"]
        self.party = wechat_conf["party"]
        self.agentid = wechat_conf["agentid"]
        self.token_url = wechat_conf["token_url"]
        self.msg_url = wechat_conf["msg_url"]

    def send(self, subject, msg):
        msg = self.normalize(msg)
        payload = {
            "touser": "",
            "toparty": self.party,
            "msgtype": "news",
            "agentid": self.agentid,
            "news": {
                "articles":
                    [
                        {
                            "title": subject,
                            "description": msg,
                            "url": "",
                            "picurl": ""
                        }
                    ]
                },
            "safe": "0"
        }
        j_str = str(payload)
        print j_str
        r = requests.post(self.msg_url + "?access_token=" + self.get_token(),
                          json=ast.literal_eval(j_str))
        print r.status_code
        print r.text
        return r

    def get_token(self):
        payload = {
            "corpid": self.corpid,
            "corpsecret": self.corpsecret
        }
        r = requests.get(self.token_url, params=payload)
        data = ast.literal_eval(r.text)
        return data["access_token"]

    def normalize(self, broker_message):
        msg = broker_message
        return msg
