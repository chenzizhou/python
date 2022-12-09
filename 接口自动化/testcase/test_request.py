# coding:utf-8
# 作者：NATURE
# 开发时间：2022/12/4 13:18
# 功能：
import json

import requests


def write_yaml():
    with open('title_name.yaml', 'w') as f:
        f.write(rep.json()['title'])


def read_yaml():
    with open('title_name.yaml', 'r') as f:
        data = f.read()
        print(data)


headers = {
    "Accept": "application/json,text/javascript, /; q=0.01",
    "X-Requested-With": "XMLHttpRequest"}

rep = requests.request('get', 'http://1.24.190.190:8091/login?redirect=%2F',
                       headers=headers)

# 返回字符串数据
print(rep.json())
# write_yaml()
# read_yaml()

# 返回字节格式的数据
# print(rep.content)
# 返回字典格式的数据
# print(rep.json())
# print(rep.status_code)
# print(rep.reason)
# print(rep.cookies)
# print(rep.encoding)
# print(rep.headers)
