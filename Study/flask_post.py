# -*- coding: utf-8 -*-
from flask import Flask,request
import json

#flask简单环境搭建
app = Flask(__name__)
@app.route('/')
def home():
    data = json.dumps({
        "username":"ran",
        "password":"111"
    })
    return data

@app.route('/post_login',methods= ['POST'])
def login():
    request_method = request.method
    #print(request_method)
    if request_method == 'POST':
        username =request.form.get("username")
        password = request.form.get("password")
        data = json.dumps({
            "username": username,
            "password": password,
            "code":"200",
            "massage":"请求成功",
            "inifo":"www.baidu.com"
        })
    else:
        data = json.dumps({
            "massage":"请求不合法"
        })
    return data

if __name__ == '__main__':
    app.run()


