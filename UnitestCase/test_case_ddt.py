# -*- coding: utf-8 -*-
import os
#获取上一级目录
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
import sys
sys.path.append(base_path)
import ddt
import unittest
from Until.handle_excel import excel_data
data = excel_data.get_excel_data()

#print(data)
#data = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]
@ddt.ddt
class TestCase01(unittest.TestCase):
    def setUp(self) -> None:
        print("case开始执行")
    def tearDown(self) -> None:
        print("case结束")
    @ddt.data(*data)
    def test_01(self,data1):
        #case编号,作用,是否执行,前置条件,依赖key,url,method	data,cookie操作,header操作,预期结果方式,预期结果,result,数据
        case_id,function,is_run,condiction,depend_key,url,method,request_data,cookie,header,execpt_method,execpet,result,result_data=data1
        #casename,casenum,isrun,method,cookies=data1
        print("this is test case",case_id,function,is_run,condiction,depend_key,url,method,request_data,cookie,header,execpt_method,execpet,result,result_data)

if __name__ == '__main__':
    unittest.main()