#coding=utf-8

import re
import requests
import json
import time
from config import headers_formobile,headers_forweb

formdata = {
    'username':'',
    'password':'',
    'savestate':'1',
    'r':'https://pad.weibo.cn/',
    'ec':'0',
    'pagerefer':None,
    'entry':'mweibo',
    'wentry':None,
    'loginfrom':None,
    'client_id':None,
    'code':None,
    'qq':None,
    'mainpageflag':'1',
    'hff':None,
    'hfp':None
}

def weilogin(username, password):
    login_url = 'https://passport.weibo.cn/sso/login'
    weibo = requests.session()
    weibo.headers.update(headers_formobile)
    formdata['username'] = username
    formdata['password'] = password
    resp = weibo.post(login_url, data=formdata)
    try:
        cross_domain_list = json.loads(resp.text)['data']['crossdomainlist']
        for key,value in cross_domain_list.items():
            cross_domain_list[key] = value.replace('\\','')
        weibo.headers.update(headers_forweb)
        weibo.get(cross_domain_list['weibo.com'])
        #weibo.get(cross_domain_list['sina.com.cn'])
        #weibo.get(cross_domain_list['weibo.cn'])
        return weibo
    except:
        return None

if __name__ == '__main__':
    weibo = weilogin('admin','123456')
