#unitest套件应用，如何同时运行多个case
import sys
sys.path.append("E:/Test/Imooc/")
from UnitestCase.test_case01 import TestCase
from UnitestCase.test_case02 import TestCase02
from UnitestCase.test_case03 import TestCase03
import unittest

case01 = unittest.TestLoader().loadTestsFromTestCase(TestCase)
case02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
case03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)
#Testsuite需要一个集合[case01,case02,case03]
suite = unittest.TestSuite([case01,case02,case03])
unittest.TextTestRunner().run(suite)

