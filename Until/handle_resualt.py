# -*- coding: utf-8 -*-
import os
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
import sys
sys.path.append(base_path)
from Until.handle_json import get_value
from deepdiff import DeepDiff

#封装获取massage
#传入的code是int类型，最后获取到的code_massage中的code为str类型，这里的code转为str
def handle_resault(url,code):
    data = get_value(url, "\Config\code_massage.json")
    if data !=None:
        for i in data:
            massage = i.get(str(code))
            if massage:
                return massage
    return None

def get_result_json(url,status):
    data = get_value(url, "/Config/result_json.json")
    if data != None:
        for i in data:
            massage = i.get(status)
            if massage:
                return massage
    return None


def handle_result_json(t1,t2):
    """"
        校验json格式,deepdiff库
    """
    if isinstance(t1,dict) and isinstance(t2,dict):
        cmp_dict = DeepDiff(t1,t2,ignore_order=True,).to_dict()
        # print(cmp_dict)
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    else:
        return False

# if __name__ == '__main__':
#     #print(handle_resault('login','10000'))
#     # dict1 = {"bbb": "333", "aaa": "222", "ccc": [{"ddd": "444"}, {"eee"}]}
#     # dict2 = {"aaa": "222", "bbb1": "333", "ccc": [{"ddd": "444"}, {"eee"}]}
#     # print(handle_result_json(dict1,dict2))
#     #print(get_result_json("api3/newcourseskill","sucess"))

