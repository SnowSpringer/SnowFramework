
#封装get，post请求
import requests,json,os
import  sys
sys.path.append('/Users/low/PycharmProjects/snowFramework/commons')

import dlog
from dlog import SnowLog

class Drequest:

    # snowLog = SnowLog()
    # snowLog.snowFileLog('INFO', os.getcwd() + '/logFile/log.log')

    def get(self,url,headers,params):
        snowLog = SnowLog()
        snowLog.snowFileLog('INFO', os.getcwd() + '/logFile/log.log')
        snowLog.snowInfo(url)
        snowLog.snowInfo(params)
        snowLog.snowInfo(headers)
        try:
            respon = requests.get(url=url,params=params)
            r_json = respon.json()
            r_status = respon.status_code
            r_totaltime = respon.elapsed.total_seconds()

            # print(r_json,type(r_json))
            # snowLog.snowInfo(r_json)
            # snowLog.snowInfo(type(r_json))
            # snowLog.snowInfo(r_status)
            # snowLog.snowInfo(r_totaltime)

            return r_status,r_json,r_totaltime

        except Exception as e:
            print('get 请求，出现异常：',e)

    def postForm(self,url,headers,params):
        # print('post请求地址:',url)
        # print('post请求参数headers{},params{}'.format(headers,params))
        snowLog = SnowLog()
        snowLog.snowFileLog('INFO', os.getcwd() + '/logFile/log.log')
        snowLog.snowInfo(url)
        snowLog.snowInfo(params)
        snowLog.snowInfo(headers)

        try:
            print(type(params))  #form表单，直接传入字典
            respon = requests.post(url=url,data=params,headers=headers)
            r_json = respon.json()
            r_status = respon.status_code
            r_totaltime = respon.elapsed.total_seconds()

            # snowLog.snowInfo(r_json)
            # snowLog.snowInfo(type(r_json))
            # snowLog.snowInfo(r_status)
            # snowLog.snowInfo(r_totaltime)

            return r_status, r_json, r_totaltime

        except Exception as e:
            print('postForm发生了异常：',e)


    def postJson(self,url,headers,params):
        # print('postJson请求地址：',url)
        # print('postJson请求参数headers{},params{}'.format(headers,params))
        # print(type(params))
        # print(params)
        snowLog = SnowLog()
        snowLog.snowFileLog('INFO', os.getcwd() + '/logFile/log.log')
        snowLog.snowInfo(url)
        snowLog.snowInfo(params)
        snowLog.snowInfo(headers)


        try:
            params = json.dumps(params)
            respon = requests.post(url = url,data= params,headers = headers)
            r_json = respon.json()
            r_status = respon.status_code
            r_totaltime = respon.elapsed.total_seconds()

            # snowLog.snowInfo(r_json)
            # snowLog.snowInfo(type(r_json))
            # snowLog.snowInfo(r_status)
            # snowLog.snowInfo(r_totaltime)

            return r_status, r_json, r_totaltime

        except Exception as e:
            print('postJson请求发生异常：',e)


# 请求，最早拿到response， 然后在其他类中 拿到json，statu_code,请求时间，但是一旦请求出错，在其他类中会报没有该方法的错误
# 优化：请求返回的数据，直接在请求封装类中，将所有需要的数据，取出来。
# 其他类中使用，直接取就可以。  有个问题，返回的是元组，其他类取时容易出错
# 更正： 其他类中从元组取出数据，需要按顺序取

