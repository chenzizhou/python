import logging
from logging import handlers

from interface_automation.commons.yaml_util import yaml_data


class LoggerHandler(logging.Logger):
    # 继承Logger类
    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format=None,
                 when='D',
                 interval=1,
                 backupCount=10,
                 encoding='utf-8',
                 ):
        # 设置收集器
        super().__init__(name)
        # 设置收集器级别
        self.setLevel(level)
        # 设置日志格式
        fmt = logging.Formatter(format)
        # 如果存在文件，就设置文件处理器，日志输出到文件
        if file:
            file_handler = handlers.TimedRotatingFileHandler(filename=file, when=when, interval=interval,
                                                             backupCount=backupCount, encoding=encoding)
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        # 设置StreamHandler,输出日志到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


# 从yaml配置文件中读取logging相关配置
logger = LoggerHandler(name=yaml_data['logger']['name'],
                       level=yaml_data['logger']['level'],
                       file='../logs/log.txt',
                       format=yaml_data['logger']['format'])
