# -*- coding: utf-8 -*-
from unittest import mock
import requests
import unittest

# url = ''
# data = {
#
# }
def post_request(url,data):
    res = requests.post(url,data).json()
    return res

class Test_Login(unittest.TestCase):
    def setUp(self):
        print("case开始执行")
    def tearDown(self):
        print("case结束")
    def test_01(self):
        url = 'https://www.imooc.com/passport/user/login'
        data = {
            "username":"1111"
        }
        success_test = mock.Mock(return_value=data)
        res= success_test
        # res = post_request
        self.assertEqual("1122",res())

if __name__ == '__main__':
    unittest.main()
