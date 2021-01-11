# -*- coding: utf-8 -*-
import requests
import unittest

class TestCase02(unittest.TestCase):
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
        print("test_01开始执行")
    def test_02(self):
        print("test_02开始执行")

if __name__ == '__main__':
    unittest.main()
    unittest.TestSuite
