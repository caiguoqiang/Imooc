import requests
import unittest
import unittest.mock

url = 'https://www.imooc.com/passport/user/login'
data = {
    "username":"caisenran",
    "password":"985721"
}
def get_req(self,url,data):
    url = 'https://www.imooc.com/passport/user/login'
    res = requests.get(url,params=data).json()
    return res
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        print("开始")
    def tearDown(self) -> None:
        print("结束")
    def test_01(self):
        url = 'https://www.imooc.com/passport/user/login'
        data = {
            "username":"1111"
        }
        get_success = unittest.mock.Mock(return_value=data)
        get_req = get_success
        res = get_req
        self.assertEqual('123',res())

if __name__ == '__main__':
    unittest.main()
