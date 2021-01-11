# -*- coding: utf-8 -*-
import os
base_path = os.getcwd()
import sys
sys.path.append(base_path)
import unittest
from Base.base_request import request

url = "http://www.imooc.com/passport/user/login"
data = {
    "username":"caisenran",
    "password":"124785"
}
host='www.imooc.com'
class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_01(self):
        res = request.run_main('post',url,data)
        print(res)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestBase('test_01'))
    unittest.TextTestRunner().run(suite)

