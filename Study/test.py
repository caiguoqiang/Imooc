import requests
import urllib3


url = "https://yyk2b.com/auth/login"
payload = {
    'act':'ajax_act_login',
    'user_name':'test',
    'password':'123457',
    'back_act':'/index.php',
    'code':'423156',
    'remember':'1'
}

urllib3.disable_warnings()
r = requests.post(url,data=payload,verify=False)
#r=requests.get(url,params=payload,verify=False)
print(r.text)
#print(r.json())
#print(r.status_code)
