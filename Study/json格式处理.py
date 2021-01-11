import requests
import json

url = 'https://www.imooc.com/activity/newcomer'
cookie = {
    "apsid":"YxMjUyMjQwYjlkNTMyNjEyZTliNDY5ODYyMGQ1Y2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANTcwNzEwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxMzE4Nzc2MTY3NkAxNjMuY29tAAAAAAAAAAAAAAAAADk1NTk0MmQ2ZDA4ZTc2ZDk4NDQ5ZmNkOWJmYzI5NWNl9KSkX4pSnl4%3DOW"
}

r=requests.get(url,cookies = cookie,verify=False)
#特别注意一定是header中返回的数据类型为json才能使用r.json(),也就是header中Accept：application/json, text/javascript, */*; q=0.01，才能使用否则报错
print(r.json())
#可以使用以下方法返回json序列化后结果或对应的编码格式
#json.loads()是将json格式对象，转化Python可识别的字典对象
#json.dumps()是将一个Python数据类型列表进行json格式的编码解析，可以将一个list列表对象，进行了json格式的编码转换
res_post = requests.post(url,cookies=cookie,verify=False)
res = json.loads(res_post.text)
res_json = json.dumps(res,indent=2)
print(res_json)
