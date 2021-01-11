# -*- coding: utf-8 -*-
import os
base_path = os.path.abspath(os.path.dirname(os.getcwd()))
import sys
sys.path.append(base_path)
from Until.handle_excel import excel_data
from Base.base_request import request
from Until.handle_resualt import handle_resault,handle_result_json,get_result_json
import json
from Until.handle_cookie import get_cookie_value,write_cookie
from Until.handle_header import get_header_value

class RunMain():
    def run_case(self):
        #获取行
        rows = excel_data.get_rows()
        #遍历行
        for i in range(rows):
            cookie = None
            get_cookie = None
            header = None
            data = excel_data.get_rows_value(i+2)
            #print(data)
            is_run = data[2]
            if is_run == 'yes':
                url = data[5]
                method = data[6]
                data1 = data[7]
                except_method = data[10]
                except_result = data[11]
                cookie_method = data[8]
                header_method = data[9]
                #print(header_method)
                #判断是否携带cookie
                if cookie_method =='yes':
                    cookie = get_cookie_value('app')
                if cookie_method=='write':
                    """
                    必须获取到cookie
                    """
                    get_cookie = {"is_cookie":"app"}
                #判断是否携带header
                if header_method =='yes':
                    header=get_header_value()
                res = request.run_main(method,url,data1,cookie,get_cookie,header)
                #print(res['errorCode'])
                code = str(res['errorCode'])
                #print(code)
                massage = res['errorDesc']
                res_json = json.dumps(res)
                if except_method=='mec':
                    config_masage = handle_resault(url,code)
                    #print("--------->massage",massage,"------------>config_massage:",config_masage)
                    if massage ==config_masage:
                        excel_data.excel_write_data(i+2,13,"成功")
                    else:
                        excel_data.excel_write_data(i+2,13,"失败")
                        res_json = json.dumps(res)
                        excel_data.excel_write_data(i+2, 14, res_json)
                if except_method=='errorcode':
                    #此处必须将excel中预期结果设置为文本形式
                    if except_result==code:
                        excel_data.excel_write_data(i+2,13,"成功")

                    else:
                        excel_data.excel_write_data(i+2,13,"失败")
                        excel_data.excel_write_data(i + 2, 14, res_json)
                if except_method == 'json':
                    if code ==1000:
                        status_str= 'success'
                    else:
                        status_str ='error'
                    expect_result = get_result_json(url,status_str)
                    result = handle_result_json(res,expect_result)
                    if result:
                        excel_data.excel_write_data(i+2,13,"成功")
                    else:
                        excel_data.excel_write_data(i+2,13,"失败")
                        excel_data.excel_write_data(i + 2, 14, res_json)


if __name__ == '__main__':
    run = RunMain()
    run.run_case()