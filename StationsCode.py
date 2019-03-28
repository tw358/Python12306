import os
import re
import json
import const
from API import API

class StationCodes(object):
    @classmethod
    def getAndSaveStationCodes(self,session): # session 还是使用Login时的session
        # 若文件存在，则直接return
        if os.path.exists(const.stationCodesFilePath):
            return
        res = session.get(API.stationCode)
        stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)',res.text) #\u4e00-\u95fa5是汉字的首尾
        # 注意编码格式utf-8
        with open(const.stationCodesFilePath, 'w', encoding='utf-8') as f:
            # ensure_ascii = False 是为了防止乱码
            f.write(json.dumps(dict(stations),ensure_ascii = False))
   
    # 获取电报码字典
    def getCodesDict(self):
        with open(const.stationCodesFilePath, 'r', encoding='utf-8') as file:
            dict = json.load(file)
            return dict