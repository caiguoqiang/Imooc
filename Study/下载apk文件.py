#coding = utf-8
import requests
import  urllib3

#下载文件
load_url = 'http://file.mukewang.com/apk/app/123/1604042633/imooc_7.4.2_10102001_android.apk?version=1604042637'

cookie = {
    "apsid":"YxMjUyMjQwYjlkNTMyNjEyZTliNDY5ODYyMGQ1Y2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANTcwNzEwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxMzE4Nzc2MTY3NkAxNjMuY29tAAAAAAAAAAAAAAAAADk1NTk0MmQ2ZDA4ZTc2ZDk4NDQ5ZmNkOWJmYzI5NWNl9KSkX4pSnl4%3DOW"
}
#不提示https警告
urllib3.disable_warnings()
r = requests.get(load_url,verify=False)
with open("mukewang.apk", "wb") as f:
    f.write(r.content)

print(r)