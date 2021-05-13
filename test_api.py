'''
创建一个本地服务用来测试框架dome内容
注释掉，文件用来作为调试dome使用
'''
import requests
import readConfig
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
from common.getToken import GetToken

'''
车证申请
'''
# 修改订单状态
url = 'https://yuanqu.sit.innoecos.cn/api/vehicle-license/dsapp/vehicle/web/apply/update'
header = GetToken().getToken()
data = {
        'id': '02f66aae5d000000',
        'applyProgress': '3'
}
e = requests.post(url=url,headers=header,data=data).text
print(e)

# #查询列表
# url = 'https://yuanqu.sit.innoecos.cn/api/vehicle-license/dsapp/vehicle/web/ticketing/list'
# header = GetToken().getToken()
# data = {
#     'paging.size':10,
#     '$filter.name':'null',
#     '$paging.page':0,
#     '$orderby':'null',
#     '$filter.params':'null,null,null,null,null'
# }
# e = requests.post(url=url,headers=header,data=data).text
# print(data)
#申请办理
# url = 'https://yuanqu.sit.innoecos.cn/api/vehicle-license/dsapp/vehicle/apply/create'
# header = {'authorization':readConfig.ReadConfig().get_content('HEADER','header')}
# print(type(header))
# data = {
#     'applyTimeCount':1,
#     'carModel': 2,
#     'carNumber':'冀H·FHFHFJ',
#     'carType':1,
#     'color':'白色',
#     'imageUrl':'aaa',
#     'phone':18814112252,
#     'companyName':'测试车证的企业',
#     'companyId':'0213ea9902c00000',
#     'userId':'0254691a43000000',
#     'projectId':'01eadbe6f4300000',
#     'parkingLotId':'1231231235',
#     'startTime' :'2021-01-11'
# }
# print(data)
# # e = RunMain().run_main('post','https://yuanqu.sit.innoecos.cn/api/vehicle-license/dsapp/vehicle/apply/create',data,readConfig.ReadConfig().get_content('HEADER','header'),'params')
# e = requests.post(url=url ,data=data,headers=header)
# print(e)


'''
用户中心获取token
'''
# a = HTTPBasicAuth('cms','123456')
# data = {
#     '$paging.size':'10',
#     '$paging.page':'1',
#     '$filter.name':'null',
#     '$orderby':'null',
#     '$filter.params':'null'
# }
# print(data)
# r = requests.post(url='https://yuanqu.sit.innoecos.cn/api/dscloud-appservice-management/web/cooperationService/list',data = data)
# print(r.json())


# a = HTTPBasicAuth('cms','123456')
# data = {
#     'username':'zhangsan',
#     'password':'12345678',
#     'grant_type':'password',
#     'scope':'all',
#     'endpoint':'app_iyou'
# }
# r = requests.get(url='https://yuanqu.sit.innoecos.cn/api/dscloud-account-center/oauth/token',auth = a,data = data)
# print(r)


'''
测试接口
'''
# from common.configHttp import RunMain
#
# data = {
#         'loginId': '15521387273',
#         'password': 'a1234567'
#     }
# result = RunMain().run_main('post', 'https://openaccount-login.aliyun.com/login/login.do?fromSite=6',data)
# print(result)
'''
----------------------------------------------------------------------------------------

'''
# import flask
# import json
# from flask import request
#
# '''
# flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服
# '''
# # 创建一个服务，把当前这个python文件当做一个服务
# server = flask.Flask(__name__)
# # @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
# @server.route('/login', methods=['get', 'post'])
# def login():
#     # 获取通过url请求传参的数据
#     username = request.values.get('name')
#     # 获取url请求传的密码，明文
#     pwd = request.values.get('pwd')
#     # 判断用户名、密码都不为空
#     if username and pwd:
#         if username == 'xiaoming' and pwd == '111':
#             resu = {'code': 200, 'message': '登录成功'}
#             return json.dumps(resu, ensure_ascii=False)  # 将字典转换字符串
#         else:
#             resu = {'code': -1, 'message': '账号密码错误'}
#             return json.dumps(resu, ensure_ascii=False)
#     else:
#         resu = {'code': 10001, 'message': '参数不能为空！'}
#         return json.dumps(resu, ensure_ascii=False)
#
# if __name__ == '__main__':
#     server.run(debug=True, port=8888, host='127.0.0.1')
#
