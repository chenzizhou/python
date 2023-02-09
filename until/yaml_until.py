# 作者
# NATURE
# 日期
# 2023/2/7 16:42
# 功能
#
import csv
import json
from contextlib import ExitStack
"""
将csv文件转换成json
"""
profileList = []
def FromCsvToJson(csv_path):
    with open(csv_path, 'r',encoding='utf-8',errors='ignore') as csv_file:
        # 以字典格式读取数据e: {'标题1':'值‘，’标题2‘：’值‘。。。，{'标题1':'值‘，’标题2‘}}，文件第一行必须是标题
        reader = csv.DictReader(csv_file)
        for row in reader:
            profileList.append(dict(row))
        return profileList

# yaml_file为YAML模板文件
# new_yaml_file为新生成的带有测试数据的YAML文件
def EnvReplaceYaml(yaml_file, new_yaml_file):
    try:
        with ExitStack() as stack:
            yml_file = stack.enter_context(open(yaml_file, 'r+'))
            yml_output = stack.enter_context(open(new_yaml_file, 'w'))
            # 先读取YAML模板文件，返回值为字符串列表
            yml_file_lines = yml_file.readlines()
            print(yml_file_lines)
            # profileList的长度即为测试用例的数量
            for i in range(0, len(profileList)):
                # 循环遍历列表
                for line in yml_file_lines:
                    new_line = line
                    # 如果找到以“$csv{”开头的字符串
                    if new_line.find('$csv{') > 0:
                        # 对字符串以“:”切割
                        env_list = new_line.split(':')
                        # 取“:”后面的部分，去掉首尾空格，再以“{”切割，再以“}”切割取出变量名称，比如“name”
                        env_name = env_list[1].strip().split('{', 1)[1].split('}')[0]
                        replacement = ""
                        # 如果name在字典列表的key里
                        if env_name in profileList[i].keys():
                            # 取出name对应的值赋给replacement
                            replacement = profileList[i][env_name]
                            # 用replacement替换掉YAML模板中的“$csv{name}”
                            for j in range(0, len(profileList)):
                                new_line = new_line.replace(env_list[1].strip(), replacement)
                    # 将new_line写入到yml_output文件里
                    yml_output.write(new_line)
                yml_output.write("\n\n")
    except IOError as e:
        print("Error: " + format(str(e)))
        raise


# csv方法介绍举例

def rowWrite01(csv_path):
    # 打开文件时加入参数newline = '', 可避免输出时每行之间多空一行
    with open(csv_path, 'w',newline='') as csvFile:
        # 写文件
        file = csv.writer(csvFile)
        file.writerow(['Name', 'Age', 'City'])
        file.writerow(['luck', '18', 'BeiJing'])
        file.writerow(['Jucy', '20', 'ShangHai'])

def rowWrite02(csv_path):
    with open(csv_path, 'w', newline='') as csvFile:
        # delimiter是分隔符，在write中，可以用分隔符更改每行之间的逗号
        file = csv.writer(csvFile, delimiter='\t')

        file.writerow(['Name', 'Age', 'City'])
        file.writerow(['luck', '18', 'BeiJing'])
        file.writerow(['Jucy', '20', 'Shan,gHai'])

def dictRowWrite(csv_path):
    with open(csv_path, 'w', newline='') as csvFile:
        # 标题
        fields = ['Name', 'Age', 'City']

        # fieldnames：设置csv文件标题
        file = csv.DictWriter(csvFile, fieldnames=fields)

        # 写入标题
        file.writeheader()
        file.writerow({'Name': 'luck', 'Age': '19', 'City': 'BeiJing'})
        file.writerow({'Name': 'Jucy', 'Age': '21', 'City': 'ShangHai'})


# csv_path='../data/test_yaml.csv'
# yaml_file='../data/yaml_file.yaml'
# new_yaml_file='../data/new_yaml_file.yaml'
# profileList=FromCsvToJson(csv_path)
# EnvReplaceYaml(yaml_file,new_yaml_file)

csv_path='../data/test.csv'
dictRowWrite(csv_path)