# -*- coding: utf-8 -*-
import requests
import json
import urllib3
import os
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
import sys
sys.path.append(base_path)
from Until.handle_ini import handle_ini
from Until.handle_cookie import write_cookie
from Until.handle_json import get_value
from Until.handle_ini import handle_ini
urllib3.disable_warnings()


class BaseRequest():
    def send_post(self,url,data,cookie=None,get_cookie=None,header = None):
        """
        发送post请求
        """
        #print(cookie)
        response = requests.post(url=url,data=data,cookies=cookie,headers=header,verify=False)
        if get_cookie !=None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res
    def send_get(self,url,data,cookie=None,get_cookie = None,header=None):
        """
        发送get请求
        """
        response = requests.get(url=url,params=data,cookies = cookie,headers =header,verify=False)
        if get_cookie !=None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res
    def run_main(self,method,url,data,cookie,get_cookie=None,header=None):
        """
        判断请求类型
        """
        #return get_value(url)

        base_url = handle_ini.get_value('host')
        if 'http' not in url:
            url = base_url + url
        print(url)
        if method == "get":
            res = self.send_get(url,data,cookie,get_cookie,header)
        else:
            res = self.send_post(url,data,cookie,get_cookie,header)
        try:
            res = json.loads(res)
        except:
            print("结果是一个text")
        #print(res)
        return res

#单例模式python独有，在这里实例化后其他地方引入后就不需要实例化
request = BaseRequest()
#if __name__ == '__main__':
    #request.run_main('get','login',"{'username':'1111'}")
