# coding:utf-8
# 作者：NATURE
# 开发时间：2022/12/4 22:01
# 功能：
import yaml
# 文件说明：yaml文件的读取与写入
import yaml


class YamlUtil:

    # 读取extract.yaml
    def read_extract_yaml(self):
        # 打开yaml文件，读取方式为a追加，编码格式utf-8， 然后重命名为 f
        with open('../extract.yaml', mode='a', encoding='utf-8') as f:
            # 读取f文件流， 读取方式FullLoader，然后赋值给value
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    # 写入extract.yaml
    def write_extract_yaml(self, data):
        # w 写入yaml文件的意思
        with open('../extract.yaml', mode='a+', encoding='utf-8') as f:
            # 写入的数据从data传入
            yaml.dump(data=data, stream=f)

    # 清空yaml文件内容
    def clear_extract_yaml(self):
        # 打开yaml文件
        with open('../extract.yaml', mode='w', encoding='utf-8') as f:
            # 清空yaml文件
            f.truncate()

    def write_yaml(self, file, data):
        with open(file, 'w') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    def read_yaml(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data


if __name__ == "__main__":
    print(YamlUtil().read_yaml('../login.yaml'))
