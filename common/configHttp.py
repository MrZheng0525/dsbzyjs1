import requests
import json
from common.Log import logger
import readConfig
from common.getToken import GetToken


logger = logger


class RunMain():

    def send_post(self, url, data, headers,badyTpe):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入,data请求为raw-json，需要进一步改进函数
        if badyTpe == 'body':
            if headers is None:
                headers = {'Content-Type': 'application/json'}
            result = requests.post(url=url, data=json.dumps(data),headers=headers).json()# 因为这里要封装post方法，所以这里的url和data值不能写死
            # print('post', result)
            res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
            return res
        elif badyTpe == 'params':
            result = requests.post(url=url, data=data,headers=headers).json()# 因为这里要封装post方法，所以这里的url和data值不能写死
            # print('post', result)
            res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
            return res

    def send_get(self, url, data, header):
        result = requests.get(url=url, params=data)
        res = json.dumps(result.json(), ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url=None, data=None, headers = None,badyType = None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        if headers is None:
            headers = {'Content-Type': 'application/json'}
        result = None
        if method == 'post':
            # print(method,url,data)
            result = self.send_post(url, data, headers,badyType)
            logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, data, headers)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result

if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    # data = {
    #     '$paging.size': '10',
    #     '$paging.page': '1',
    #     '$filter.name': 'null',
    #     '$orderby': 'null',
    #     '$filter.params': 'null'
    # }
    data = {
        'applyTimeCount':'1',
        'carModel': '2',
        'carNumber':'冀H·FHFHFJ',
        'carType':'1',
        'color':'白色',
        'imageUrl':'["https://dscloud-digitalmaint-iyou-test-1.oss-cn-beijing.aliyuncs.com/data/ceb5d5hhcd9g8afg5bb88a85hag679aa_1610348788468.png"]',
        'phone':'18814112253',
        'companyName':'测试车证的企业',
        'companyId':'0213ea9902c00000',
        'userId':'0254691a43000000',
        'projectId':'01eadbe6f4300000',
        'parkingLotId':'1231231235',
        'startTime':'2021-01-11'
    }
    header = GetToken().getToken()
    url = 'https://yuanqu.sit.innoecos.cn/api/vehicle-license/dsapp/vehicle/apply/create'
    e = RunMain().run_main('post',url,data,header,'params')
    # e =requests.post(url=url,data=data,headers=header).text
    print(e)