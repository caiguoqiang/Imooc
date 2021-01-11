#coding = utf-8
import requests
import  urllib3

#上传文件
url_post = 'https://www.imooc.com/user/postpic'
#url_get = ''
#Content-Disposition: form-data; name="fileField"; filename="08f790529822720e616d108870cb0a46f21fab25.jpg"
#Content-Type: image/jpeg
#Content-Disposition: form-data; name="type"
file = {
    #"fileField":("文件名",open("路径","打开方式"),"文件类型"),
    "fileField":("ym.jpg",open("C:/Users/Alex/Desktop/ym.jpg","rb"),"image/jpg"),
    "type":1
}
cookie = {
    "apsid":"YxMjUyMjQwYjlkNTMyNjEyZTliNDY5ODYyMGQ1Y2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANTcwNzEwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxMzE4Nzc2MTY3NkAxNjMuY29tAAAAAAAAAAAAAAAAADk1NTk0MmQ2ZDA4ZTc2ZDk4NDQ5ZmNkOWJmYzI5NWNl9KSkX4pSnl4%3DOW"
}
#不提示https警告
urllib3.disable_warnings()
r = requests.post(url_post,files=file,cookies = cookie,verify=False).text
print(r)