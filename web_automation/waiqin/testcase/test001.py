# coding:utf-8
# 作者：NATURE
# 开发时间：2022/12/4 15:15
# 功能：
import os
env_dist = os.environ

for key in env_dist:
    if 'allure' in env_dist[key]:
        print(key + '：env_distKey的值------------' + env_dist[key])