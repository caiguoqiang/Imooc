# -*- coding: utf-8 -*-
import os
#获取上一级目录
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
# print(base_path)
import sys
sys.path.append(base_path)
import json
from Until.handle_json import read_json,write_value

def get_header_value():
    data = read_json("/Config/header.json")
    #print(data)
    return data