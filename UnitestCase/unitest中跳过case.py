import unittest

class TestCase001(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_01(self):
        print("01执行")
    def test_02(self):
        print("02执行")
    def test_03(self):
        print("03执行")
    #跳过这个case'不执行
    @unittest.skip("这个case不执行")
    def test_04(self):
        print("04执行")
    #判断该条case是否执行,条件成立则不执行，条件不成立则执行（5>9，不成立，则执行该条case；5>4，成立，则不执行）
    @unittest.skipIf(4<8,"4大于8不执行")
    def test_05(self):
        print("05执行")

if __name__ == '__main__':
    unittest.main()