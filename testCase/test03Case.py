import json
import unittest

from common import configDB
from common.configHttp import RunMain
import paramunittest
import geturlParams
import readExcel
from common.getToken import GetToken
import readConfig

'''
车证办理流程
'''
url = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
dataCase_xls = readExcel.readExcel().get_xls('carCase.xlsx', 'apply')

class G():
    global applyId

@paramunittest.parametrized(*dataCase_xls)
class testUserCreat(unittest.TestCase):
    def setParameters(self, case_name, path, query, method, body_type, code, assertKey,date):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.bady_type = str(body_type)
        self.code = code
        self.assertKey = assertKey
        self.date = str(date)
        self.header = GetToken().getToken()
        #获取默认的156token

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
        global ss
        data = eval(self.query)
        bodyType = self.bady_type
        headers = self.header
        url1 = url +self.path
        try:
            # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
            info = RunMain().run_main(self.method, url1, data, headers,bodyType)
            ss = json.loads(info)# 将响应转换为字典格式
        except:
            print('请求结果转换json失败')
        if self.case_name == 'applyCarAttend':
            self.assertEqual(ss[self.assertKey], self.code)
            G.applyId = ss['data']
            print(G.applyId)
            key = 'apply_progress'
            table = 'vehicle_license_apply_info'
            conditions = 'id'
            value = G.applyId
            a = configDB.DBsql(readConfig.ReadConfig().get_content('DATABASE','host'),
                           readConfig.ReadConfig().get_content('DATABASE','user'),
                           readConfig.ReadConfig().get_content('DATABASE','password'),
                           readConfig.ReadConfig().get_content('DATABASE','databaseCar')).Select(key,table,conditions,value)
            self.assertIn('1',str(a))
        elif self.case_name == 'getCarList':
            self.assertEqual(ss[self.assertKey],self.code)
            self.assertEqual(ss['success'],True)
        elif self.case_name == 'updateType3':
            self.assertEqual(ss[self.assertKey],self.code)
            key = 'apply_progress'
            table = 'vehicle_license_apply_info'
            conditions = 'id'
            value = G.applyId
            a = configDB.DBsql(readConfig.ReadConfig().get_content('DATABASE', 'host'),
                               readConfig.ReadConfig().get_content('DATABASE', 'user'),
                               readConfig.ReadConfig().get_content('DATABASE', 'password'),
                               readConfig.ReadConfig().get_content('DATABASE', 'databaseCar')).Select(key, table,
                                                                                                      conditions, value)
            self.assertIn('3', str(a))
        elif self.case_name == 'updateType4':
            self.assertEqual(ss[self.assertKey], self.code)
            key = 'apply_progress'
            table = 'vehicle_license_apply_info'
            conditions = 'id'
            value = G.applyId
            a = configDB.DBsql(readConfig.ReadConfig().get_content('DATABASE', 'host'),
                            readConfig.ReadConfig().get_content('DATABASE', 'user'),
                            readConfig.ReadConfig().get_content('DATABASE', 'password'),
                            readConfig.ReadConfig().get_content('DATABASE', 'databaseCar')).Select(key, table,
                                                                                                      conditions, value)
            self.assertIn('4', str(a))
        elif self.case_name == 'updateType4':
            self.assertEqual(ss[self.assertKey],self.code)
        elif self.case_name == 'getUserList':
            self.assertEqual(ss[self.assertKey],self.code)
            self.assertNotEqual(len(ss['data']),0)
        elif self.case_name == 'end':
            table = 'vehicle_license_apply_info'
            conditions = 'id'
            value = G.applyId
            configDB.DBsql(readConfig.ReadConfig().get_content('DATABASE', 'host'),
                           readConfig.ReadConfig().get_content('DATABASE', 'user'),
                           readConfig.ReadConfig().get_content('DATABASE', 'password'),
                           readConfig.ReadConfig().get_content('DATABASE', 'databaseCar')).Delete(table,conditions,value)


if __name__ == '__main__':
    unittest.TestCase()