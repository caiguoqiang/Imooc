import sys
import os
#sys.path.append("E:/Test/Imooc/")
import unittest

#pycharm中直接获取的就是case路径
case_path = os.getcwd()
print(case_path)
discovers = unittest.TestLoader().discover(case_path,pattern='test*.py')
print(discovers)
unittest.TextTestRunner().run(discovers)
