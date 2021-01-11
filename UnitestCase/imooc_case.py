# -*- coding: utf-8 -*-
import os
#获取上一级目录
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
print(base_path)
import sys
sys.path.append(base_path)
"""
每次设置先在前部分添加如上几行代码，保证path路径正确
"""
import unittest
import urllib3
from Base.base_request import request
import json
from unittest import mock
import HTMLTestRunner

"""
unitest结合mock使用
"""
host = 'https://www.imooc.com'
"""
为方便管理多case，在接送文件中同时设置多json，通过key，value形式来获取对应的值
"""
#获取json文件
def read_json():
    with open(base_path+'\config\imooc_json.json') as f:
        #传的是json文件使用load
        data = json.load(f)
    return data
#传入key值获取对应value值即获取这个接口地址对应的json内容
def get_value(key):
    data = read_json()
    return data[key]

class ImoocCase(unittest.TestCase):
    def test_redpacketinfo(self):
        url = host+'/activity/redpacketinfo'
        data = {
            'marking':'redpacket2020'
        }
        #通过传入接口获取对应的json值
        read_method = mock.Mock(return_value=get_value('activity/redpacketinfo'))
        request.run_main=read_method
        res = request.run_main('post',url,data)
        urllib3.disable_warnings()
        print(json.dumps(res,indent=2))
        self.assertEqual(res['errorCode'],1000,msg="访问失败")

if __name__ == '__main__':
    #生成报告不能直接使用unitest执行，需要使用python执行
    file_path = base_path+'\Report'
    suite = unittest.TestSuite()
    suite.addTest(ImoocCase('test_redpacketinfo'))
    with open(file_path+'\\report.html',"wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="test report",description="caisenran report")
        runner.run(suite)
    f.close()
