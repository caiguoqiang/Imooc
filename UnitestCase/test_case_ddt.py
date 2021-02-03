# -*- coding: utf-8 -*-
import os
#获取上一级目录
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
import sys
sys.path.append(base_path)
import ddt
import unittest

data = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]
@ddt.ddt
class TestCase01(unittest.TestCase):
    def setUp(self) -> None:
        print("case开始执行")
    def tearDown(self) -> None:
        print("case结束")
    @ddt.data(*data)
    def test_01(self,data1):
        casename,casenum,isrun,method,cookies=data1
        print("this is test case",casename,casenum,isrun,method,cookies)


if __name__ == '__main__':
    unittest.main()