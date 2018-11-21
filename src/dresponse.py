import sys

sys.path.append('/Users/low/PycharmProjects/snowFramework/src')

from src import drequest
import drequest
from drequest import Drequest
import json,re
import requests


class DreponseF:
    def Dreponse(self,method,url,headers,params,checkPoint):

        snow = Drequest()
        if method == 'get':
            r = snow.get(url = url,headers=headers,params = params)
        elif method == 'post' and headers == {"content-type":"application/x-www-form-urlencoded"}:
            r = snow.postForm(url= url,headers = headers,params = params)
        elif method == 'post' and headers == {"content-type":"application/json"}:
            r = snow.postJson(url= url,headers = headers,params = params)
        else:
            print(method,url,headers,params)

        # try:
        #     print(r)
        #     print(r[0])
        #     print(r[1])
        #     print(r[2])
        #
        #     print('哈哈，以上是循环判断 调用get，post类的打印哦')
        # except:
        #     print('哈哈哈哈让大家放心')

        return r

# 发现此类中调用的Drequest 中postForm请求方法，返回的是响应数据体，
# 但是 在该类中打印响应http请求，print(r.statu_code)， 打印响应时长，print(r.elapsed.total_time) 一直打印错误
# 找到错误原因，print(r.status_code)  正确语句是status_code , 没有联想，自己手动少输入 s
# 由于没在上一层类中，没有联想功能，自己第一次打错，后来再打时，该类联想的是自己的错误输入

# 响应时间，错误原因一样。 没有联想，没去上一层查看，直接输入的r.elapsed.total_time， 其实正确的是r.elapsed.total_seconds()