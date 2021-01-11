# -*- coding: utf-8 -*-
import os
#获取上一级目录
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
# print(base_path)
import sys
sys.path.append(base_path)
import json
from Until.handle_json import read_json,write_value


"""
    1、获取cookie
    2、写入cookie
    3、是否携带cookie（runmain汇总判断）
"""
def get_cookie_value(cookie_key):
    """
    获取cookie
    :param cookie_key:
    :return:
    """
    data = read_json("/Config/cookie_json.json")
    return data[cookie_key]

def write_cookie(data,cookie_key):
    """
    写入cookie
    :param data:
    :param cookie_key:
    :return:
    """
    data1 = read_json("/Config/cookie_json.json")
    data1[cookie_key] = data
    write_value(data1)




if __name__ == '__main__':
    print(get_cookie_value('app'))
    data={
        "app":{
        "dddd":"1111"
    }
    }
    write_cookie(data,'app')
