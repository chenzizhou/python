# coding=utf-8
import configparser
from typing import Text
from selenium.webdriver.common import keys
import sys
import os
filename=r'E:\python_script\chandao\config\localElement.ini'
class ReadIni():
    def __init__(self,filename=None,node=None):
        self.cf=configparser.ConfigParser()
        if filename==None:
            filename=r'E:\python_script\chandao\config\localElement.ini'
            self.loadIni(filename)
        else:
             self.loadIni(filename)
        if node==None:
            self.node='login'
        else:
            self.node=node
    def loadIni(self,filename):
        self.cf.read(filename,encoding="utf-8-sig")
    def get_value(self,key):
        data=self.cf.get(self.node,key)
        return data
if __name__=='__main__':
    print(sys.path)
    print(os.getcwd())
    print(os.path.abspath('1.txt'))

