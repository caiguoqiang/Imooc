# -*- coding: utf-8 -*-
import requests
import unittest

class TestCase03(unittest.TestCase):
    def setUp(self):
        print("setup开始执行")
    def tearDown(self):
        print("tear执行结束")
    @classmethod
    def setUpClass(cls):
        print("class开始执行")
    @classmethod
    def tearDownClass(cls):
        print("class结束执行")
    def test_01(self):
        print("test_01开始执行")
    def test_02(self):
        print("test_02开始执行")

if __name__ == '__main__':
    unittest.main()

