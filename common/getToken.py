import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import json
import readConfig

'''
默认获取15630937273的token
可以选择获取相应用户token
'''

a = HTTPBasicAuth('cms','123456')
url = 'https://yuanqu.sit.innoecos.cn/oauth/token'

class GetToken():

    def getToken(self ,admin = None , password = None):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入,data请求为raw-json，需要进一步改进函数
        if admin is None and password is None :
            self.admin = str('15630937273')
            self.password = 'a123456a'
        else:
            self.admin = admin
            self.password = password
        data = {
            'username':self.admin,
            'password':self.password,
            'grant_type':'password',
            'scope':'all',
            'endpoint':'app_iyou'
        }
        #等用户中心上线，使用request获取token
        try:
            result = requests.post(url=url, data=json.dumps(data),auth=a).json()# 因为这里要封装post方法，所以这里的url和data值不能写死
            res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        except:
            pass
        token = {
            'authorization':readConfig.ReadConfig().get_content('HEADER','header')
        }
        return token


if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    e = GetToken().getToken('123456','789654')
    print(e)