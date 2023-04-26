import random
import time

from interface_automation.commons.yaml_util import YamlUtil


class DebugTalk:

    # 获得随机数
    def get_randon_number(self, min, max):
        return random.randint(int(min), int(max))

    # 获取随机时间
    def get_random_time(self):
        # return str(int(time.time()))[1:6]     #获取随机时间，得到的是时间戳
        return time.strftime('%H:%M:%S', time.localtime(time.time()))  # 获取本地时间，并将格式转换成时分秒

    # 读取extract.yaml文件中的值
    def read_extract_data(self, key):
        return YamlUtil().read_extract_yaml(key)

