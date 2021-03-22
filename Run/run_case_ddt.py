# -*- coding: utf-8 -*-
import os
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
import sys
sys.path.append(base_path)
import ddt
import unittest
from Until.handle_excel import excel_data
from Until.condition_data import get_data
from Until.handle_excel import excel_data
from Base.base_request import request
from Until.handle_resualt import handle_resault,handle_result_json,get_result_json
import json
from Until.handle_cookie import get_cookie_value,write_cookie
from Until.handle_header import get_header_value
import urllib3
import HTMLTestRunner

urllib3.disable_warnings()
data = excel_data.get_excel_data()

@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):
    @ddt.data(*data)
    def test_main_case(self,data):
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        is_run = data[2]
        case_id = data[0]
        i = excel_data.get_rows_number(case_id)
        if is_run == 'yes':
            try:
                url = data[5]
                method = data[6]
                is_depend = data[3]
                data1 = json.loads(data[7])
                if is_depend:
                    # 获取依赖数据
                    depend_key = data[4]
                    depend_data = get_data(is_depend)
                    #print(depend_data)
                    data1[depend_key] = depend_data

                except_method = data[10]
                except_result = data[11]
                cookie_method = data[8]
                header_method = data[9]
                # print(header_method)
                # 判断是否携带cookie
                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    """
                    必须获取到cookie
                    """
                    get_cookie = {"is_cookie": "app"}
                # 判断是否携带header
                if header_method == 'yes':
                    header = get_header_value()
                res = request.run_main(method, url, data1, cookie, get_cookie, header)
                # print(res['errorCode'])
                code = str(res['errorCode'])
                # print(code)
                massage = res['errorDesc']

                #maasge+errorcode判断返回时massage与config是否一致
                res_json = json.dumps(res)

                if except_method == 'mec':
                    config_masage = handle_resault(url, code)
                    """
                    # print("--------->massage",massage,"------------>config_massage:",config_masage)
                    if massage == config_masage:
                        excel_data.excel_write_data(i, 13, "成功")
                    else:
                        excel_data.excel_write_data(i, 13, "失败")
                        res_json = json.dumps(res)
                        excel_data.excel_write_data(i, 14, res_json)
                """
                    try:
                        self.assertEqual(massage,config_masage)
                        excel_data.excel_write_data(i, 13, "成功")
                    except Exception:
                        excel_data.excel_write_data(i, 13, "成功")
                        res_json = json.dumps(res)
                        excel_data.excel_write_data(i, 14, res_json)
                        raise Exception

                if except_method == 'errorcode':
                    """
                    # 此处必须将excel中预期结果设置为文本形式
                    if except_result == code:
                        excel_data.excel_write_data(i + 2, 13, "成功")
    
                    else:
                        excel_data.excel_write_data(i, 13, "失败")
                        #失败会回写数据
                        excel_data.excel_write_data(i, 14, res_json)
                    """
                    try:
                        self.assertEqual(except_result,code)
                        excel_data.excel_write_data(i + 2, 13, "成功")
                    except Exception:
                        excel_data.excel_write_data(i, 13, "失败")
                        res_json = json.dumps(res)
                        excel_data.excel_write_data(i, 14, res_json)
                        raise Exception
                if except_method == 'json':

                    if code == 1000:
                        status_str = 'success'
                    else:
                        status_str = 'error'
                    expect_result = get_result_json(url, status_str)
                    result = handle_result_json(res, expect_result)
                    """
                    if result:
                        excel_data.excel_write_data(i, 13, "成功")
                    else:
                        excel_data.excel_write_data(i, 13, "失败")
                        excel_data.excel_write_data(i, 14, res_json)
                    """
                    try:
                        self.assertTrue(result)
                        excel_data.excel_write_data(i, 13, "成功")
                    except Exception:
                        excel_data.excel_write_data(i, 13, "失败")
                        res_json = json.dumps(res)
                        excel_data.excel_write_data(i, 14, res_json)
                        raise Exception
            except Exception as e:
                excel_data.excel_write_data(i, 13, "失败")
                raise e

if __name__ == '__main__':
    case_path = base_path + "\\Run"
    report_path = base_path + "\\Report\\report.html" #E:\Test\Imooc\Report\report.html
    discover = unittest.defaultTestLoader.discover(case_path, pattern="run_case_*.py")
    # unittest.TextTestRunner().run(discover)
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="caishenran", description="this is test")
        runner.run(discover)

