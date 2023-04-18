# coding:utf-8
# 作者：NATURE
# 开发时间：2022/12/4 22:01
# 功能：
import yaml

file = '../testcase/title_name.yaml'
data = {'people': {'name': 'nature', 'age': 22}}


def write_yaml(file, data):
    with open(file, 'w') as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)


def read_yaml(file):
    with open(file, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


login = {
    'name': '登录',
    'request':
        {
            'url': 'http://10.41.16.20:32091/hbp/userService/login?&type=1&sys=PATROL&sysVersion=&operSys=Windows&client=Chrome%3A%20114.0.0.0&platformType=pc&userAndPwd=LAXnCU%2BPweQ8Z8ryECP0CVw5PwCbnUHwN%2FYhtHctZyMP9Wd%2B2VPO7L4c3v%2Bn62IlKehNPd6kWG2mQmIIwqcUNOtWi71TxyrzQZhWvDlAA1bNXJmF9NiQVqDm9MUqs0zB4tdp8RF%2BduPH3EKSnXcDPtFETySr5Hksmdhkjo5Pius%3D&access_token=',
            'method': 'get',
            'data': ''
        },
    'validate': ''
}
# data = read_yaml('../testcases/title_name.yaml')
# print(data)
file = '../login.yaml'
write_yaml(file, login)
