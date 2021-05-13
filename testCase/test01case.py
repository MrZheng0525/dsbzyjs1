import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
# import pythoncom
import readExcel
# pythoncom.CoInitialize()

"""
    用例包括合作商户：创建，查找
"""
url = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
dataCase_xls = readExcel.readExcel().get_xls('serviceCase.xlsx', 'creat')

@paramunittest.parametrized(*dataCase_xls)
class testUserCreat(unittest.TestCase):
    def setParameters(self, case_name, path, query, method, body_type, code, assertKey,data):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :param data 结果断言
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.bady_type = str(body_type)
        self.code = code
        self.assertKey = assertKey
        self.data = str(data)

    def description(self):
        """
        test report description
        :return:
        """
        var = self.case_name


    def setUp(self):
        """
        :return:
        """
        print("测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        #------使用eval方法将参数str类型转换为dict
        data = eval(self.query)
        bodyType = self.bady_type
        headers = None
        url1 = url +self.path
        # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        # data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        # print(self.method,url,data)

        info = RunMain().run_main(self.method, url1, data, headers, bodyType)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)# 将响应转换为字典格式
        self.assertEqual(ss[self.assertKey], self.code)
        # if self.case_name == 'list_less2':
        #     self.assertEqual(ss['data']['id'],'2000')


if __name__ == '__main__':
    unittest.TestCase()