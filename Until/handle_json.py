import os
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
import sys
sys.path.append(base_path)
import json

#获取json文件
def read_json(file_name= None):
    # 如果传入file_name=\Config\code_massage.json，则获取code_nassage中的值用于判断code与massage是否对应
    #若没有传入则获取imooc_json.json,获取接口返回值
    if file_name ==None:
        file_path = base_path+'\Config\imooc_json.json'
    else:
        file_path = base_path+file_name
    with open(file_path,encoding='utf-8') as f:
        #传的是json文件使用load
        data = json.load(f)
    return data
#传入key值获取对应value值即获取这个接口地址对应的json内容
#如果传入file_name，则获取code_nassage中的值用于判断code与massage是否对：
def get_value(key,file_name = None):
    data = read_json(file_name)
    #使用data[key]则当不存在Key值时报 KeyError
    #return data[key]
    #使用data.get(key)则当不存在Key值时报TypeError,推荐使用
    return data.get(key)

def write_value(data):
    """
    可能涉及多个cookie，cookie_json中设计多种cookie，则在write中根据参数不同获取对用cookie
    :return:
    """
    data_value = json.dumps(data)
    with open(base_path+"/Config/cookie_json.json","w+") as f:
        f.write(data_value)


