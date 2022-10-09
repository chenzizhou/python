# coding:utf-8
# 作者：NATURE
# 开发时间：2022/10/9 20:40
# 功能：
import requests

# req=requests.request(method='get',url='http://www.baidu.com')
data = {'ecode': 'ZC', 'init': 'ZC'}
req = requests.get(url='http://10.41.16.20:32091', params=data)
print(req.json())
