#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
import importlib
import urllib
import urllib.request
import optparse
import json
import httplib2
from http import cookiejar
from urllib.parse import urlencode

#reload(sys) #用于重新载入之前载入的模块。

def Login():
    cj = cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)

    print ("--------------[step1] to get cookie")
    Url = "https://kyfw.12306.cn/otn/resources/login.html"
    resp = urllib.request.urlopen(Url)
    for index, cookie in enumerate(cj):
        print ('[',index, ']',cookie)

    print ("--------------[step2] to get code")
    Url2 = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.1286778988351791"
    resp2 = urllib.request.urlopen(Url2)


    with open("code.png", "wb") as image:
        image.write(resp2.read())
         
    codeStr = sys.stdin.readline()
    codeStr = codeStr[:-1]
     
    print ('--------------[step3] to check code')
    ajax_url = "https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsyn"
    dc = {
        'randCode'      :  codeStr,
        'rand'      : "sjrand"
    }
    request = urllib.request.Request(ajax_url, urllib.parse.urlencode(dc))
    request.add_header("Content-Type", "application/x-www-form-urlencoded; charset=utf-8")
    request.add_header('X-Requested-With','XMLHttpRequest')
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    request.add_header('Referer','https://kyfw.12306.cn/otn/login/init')
    request.add_header('Accept','*/*')
    request.add_header('Accept-Encoding','gzip, deflate')
 
    f = urllib.request.urlopen(request) 
    print(f.read())
 
 
    print ("--------------[step4] to login")
    LoginUrl = "http://kyfw.12306.cn/otn/login/loginAysnSuggest"
    dc = {
         'randCode'      :  codeStr,
         'userDTO.password'     : "sunyuke1989",
        'loginUserDTO.user_name': "sunyuke@qq.com"
    };
    req = urllib.request.Request(LoginUrl, urllib.parse.urlencode(dc))
    req.add_header('Content-Type', "application/x-www-form-urlencoded")
    req.add_header('X-Requested-With','XMLHttpRequest')
    req.add_header('Origin','https://kyfw.12306.cn')
    req.add_header('Referer','https://kyfw.12306.cn/otn/login/init')
    req.add_header('Accept','*/*')
    req.add_header('Accept-Encoding','gzip, deflate')
    req.add_header('Connection','keep-live')
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    resp = urllib.request.urlopen(req)
    print(resp.read().encode('gb18030'))
 
 
    LoginingUrl = "https://kyfw.12306.cn/otn/login/userLogin"
    req = urllib.request.Request(LoginingUrl, "")
 
    print ("--------------[step5] to QueryUserInfo")
    LoginingUrl = "https://kyfw.12306.cn/otn/modifyUser/initQueryUserInfo"
    req = urllib.request.Request(LoginingUrl, "")
    resp = urllib.request.urlopen(req)
    info = resp.read()
    print(resp.read().encode('gb18030'))






if __name__=="__main__": 
    Login()