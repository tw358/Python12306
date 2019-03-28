from datetime import datetime
from StationCodes import StationCodes
from Color import Color
import time
import requests

class Utility(object):

    @classmethod
    def getSession(self):
        session = requests.session()  # 创建session会话

        session.headers = {

            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }
        # session.verify = False  # 跳过SSL验证
        return session
    
    @classmethod
    def redColor(self,str):
        return  Color.red(str)