# -*- coding: utf-8 -*-
import os
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
import sys
sys.path.append(base_path)
import configparser
# file_path = base_path+'\\Config\\server.ini'
#
# config = configparser.ConfigParser()
# config.read(file_path,encoding='utf-8')
# data = config.get('server','host')
# print(data)

class HandleInit():
    def load_ini(self):
        """
        加载ini文件
        :return:
        """
        file_path = base_path+'\Config\\server.ini'
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding='utf-8')
        return cf
    def get_value(self,key,section = None):
        """
        拿到对应值
        :return:
        """
        if section==None:
            section = 'server'
        try:
            data = self.load_ini().get(section,key)
        except Exception:
            #当没有获取到该值时抛出异常，并赋值data为None
            print("没有获取到值")
            data =None
        return data

handle_ini=HandleInit()
# if __name__ == '__main__':
#     print(handle_ini.get_data('host'))
#     print(handle_ini.get_data('local'))
