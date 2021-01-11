import requests

url = 'https://www.imooc.com/search/hotwords'
cookie = {
    "apsid":"apsid=YxMjUyMjQwYjlkNTMyNjEyZTliNDY5ODYyMGQ1Y2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANTcwNzEwMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxMzE4Nzc2MTY3NkAxNjMuY29tAAAAAAAAAAAAAAAAADk1NTk0MmQ2ZDA4ZTc2ZDk4NDQ5ZmNkOWJmYzI5NWNl9KSkX4pSnl4%3DOW"
}
header = {
"Accept": "application/json, text/javascript, */*; q=0.01",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
"X-Requested-With":"XMLHttpRequest",
"Origin": "https://www.imooc.com",
}

r=requests.post(url,cookies = cookie,headers=header,verify=False)
print(r.json())