# coding:utf-8
# 作者：NATURE
# 开发时间：2022/12/4 22:01
# 功能：
import yaml

file = '../testcase/title_name.yaml'
data = {'people': {'name': 'nature', 'age': 22}}


def write_yaml(file, data):
    with open(file, 'w') as f:
        yaml.dump(data=data,stream=f,allow_unicode=True)


def read_yaml(file):
    with open(file, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data


data = read_yaml('../testcase/title_name.yaml')
print(data)
# write_yaml(file,data)
