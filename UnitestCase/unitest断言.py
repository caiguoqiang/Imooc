# -*- coding: utf-8 -*-
import requests
import unittest

url = 'http://www.baidu.com'
data = {
    "username":"11111",
    "password":"22222"
}
class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("setup开始执行")
    def tearDown(self) -> None:
        print("tear执行结束")
    @classmethod
    def setUpClass(cls) -> None:
        print("class开始执行")
    @classmethod
    def tearDownClass(cls) -> None:
        print("class结束执行")
    def test_01(self):
        res = requests.get(url=url)
        data1 = {
            "username":"3333"
        }
        self.assertEqual(res,data1)
    def test_02(self):
        data1 = {
            "username": "3333"
        }
        self.assertDictEqual(data1,data,msg="这两个值不相等")

if __name__ == '__main__':
    unittest.main()
