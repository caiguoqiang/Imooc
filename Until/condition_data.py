# -*- coding: utf-8 -*-
import os
#获取上一级目录
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
import sys
sys.path.append(base_path)
from Until.handle_excel import excel_data
import json
from jsonpath_rw import jsonpath,parse

def spilt_data(data):
    #imooc_005>data:banner:id
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id,rule_data

def depend_data(data):
    """
    获取依赖结果集
    :param data:
    :return:
    """
    case_id = spilt_data(data)[0]
    rows_number = excel_data.get_rows_number(case_id)
    data = excel_data.get_cell_value(rows_number,14)
    return data

def get_depend_data(res_data,key):
    """
    获取依赖字段
    :param res_data:
    :param key:
    :return:
    """
    print(type(res_data))
    res_data = json.loads(res_data)
    json_exe = parse(key)
    madle = json_exe.find(res_data)
    return [math.value for math in madle][0]

def get_data(data):
    """
    获取依赖数据
    :param data:
    :return:
    """
    #print(type(data))
    res_data = depend_data(data)
    #print(type(res_data))
    rule_data =spilt_data(data)[1]
    return get_depend_data(res_data,rule_data)


#if __name__ == '__main__':
    # print(depend_data("imooc_005>data.banner.id"))
    # data = {
    #     "a":"a1",
    #     "b":"b1",
    #     "c":[
    #         {
    #             "d":"d1"
    #         },
    #         {
    #             "d":"d2"
    #         }
    #     ]
    # }
    # key="c.[1].d"
    # print(get_depend_data(data,key))