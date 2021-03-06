#from codePlatform import  CJYClient
import sys
class Const(object):
    class ConstError(TypeError): pass
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstError("Changing const.%s" % key)
        else:
            self.__dict__[key] = value
    def __getattr__(self, key):
        if key in self.__dict__:
            return self.key
        else:
            return None
sys.modules[__name__] = Const()


# 12306登录用户名
userName = '你的12306账号'
# 12306密码
password = '你的12306密码'
# 超级鹰打码平台
chaoJiYing = "123"
#chaoJiYing = CJYClient('你的超级鹰平台账户', '你的超级鹰平台密码','896970')
# 验证码图片路径
captchaFilePath = 'captcha.jpg'
# 车站电报码路径
stationCodesFilePath = 'stationsCode.txt'
# 座位类型，订票下单时需要传入
noSeat            = 'WZ' #无座
firstClassSeat    = 'M'  #一等座
secondClassSeat   = 'O'  #二等座
advancedSoftBerth = '6'  #高级软卧 A6
hardBerth         = '3'  #硬卧 A3
softBerth         = '4'  #软卧 A4
moveBerth         = 'F'  #动卧
hardSeat          = '1'  #硬座 A1
businessSeat      = '9'  #商务座 A9