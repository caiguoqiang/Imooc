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
        flag = False
        self.assertTrue(flag,msg="判断正确为True")
    def test_02(self):
        data1 = {
            "username": "3333"
        }
        self.assertDictEqual(data1,data,msg="这两个值不相等")

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    """
    suite.addTest(TestCase('test_02'))
    suite.addTest(TestCase('test_01'))
    """

    tests = [TestCase('test_02'),TestCase('test_01')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner().run(suite)
