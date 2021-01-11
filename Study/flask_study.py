# -*- coding: utf-8 -*-
from flask import Flask,request
import json

#flask简单环境搭建
app = Flask(__name__)
@app.route('/')
def home():
    data = json.dumps({
        "username":"caisenran",
        "password":"111111"
    })
    return data

@app.route('/pass',methods= ['GET'])
def login():
    username =request.args.get("username")
    password = request.args.get("password")
    if username and password:
        data = json.dumps({
            "username": username,
            "password": password,
            "code":"200",
            "massage":"请求成功",
            "inifo":"www.baidu.com"
        })
    else:
        data = json.dumps({
            "massage":"参数错误"
        })
    return data

if __name__ == '__main__':
    app.run()
