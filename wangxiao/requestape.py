import requests
from Excel import datainfo
import os
from file_phont import updateImage
from cfg import *
import re
import json
class requestApi:
    def __init__(self):
        self.R = requests
        self.excel_data = datainfo()
        self.data = self.excel_data.get_row_data()
        photo_path = os.path.dirname(__file__)
        photo_path = photo_path + "/file_path/600.jpg"
        #关联字典
        self.photo_url = updateImage(photo_path,"600.jpg")
        self.photo_url = self.photo_url["data"]["path"]
        self.mobil = mobile
        self.correlationDict = {
            "${phtoto_url}":self.photo_url
        }

    def get_function(self,method,api_url,api_headers,api_data=None):
        if method == 'GET':
            response = self.R.get(api_url, data=api_data,headers=api_headers)

            return response

        elif method == 'POST':
            response = self.R.post(api_url, data=api_data, headers=api_headers)

            return response

        elif method == 'DELETE':
            response = self.R.delete(api_url,headers=api_headers)
            return response

        elif method == 'PUT':
            response = self.R.put(api_url,data=api_data,headers=api_headers,)
            return response

        else:
            pass

    def api_requests(self, api_no,api_url,
                     api_function, api_data,
                     api_correlation):
        '''
           公用请求方法
           :param api_no       : 接口编号
           :param api_name     : 接口名称
           :param api_describe : 接口描述
           :param api_url      : 接口地址
           :param api_function : 接口方法
           :param api_headers  : 接口头部
           :param api_data     : 接口数据
           :param api_check    : 接口检查
           :param api_hope     : 接口预期
           :return             : 接口返回 response[0] - 状态码 | response[1] - 返回值
        '''
        self.correlationDict["${nowtime}"]= nowtime()
        self.correlationDict["${mobile}"] = self.mobil
        if api_data=='':
            self.url = "https://testwx.baijiayun.com" + self.analysis_url(api_url)
            self.api_headers = headers
            response = self.get_function(
                method=api_function,
                api_url=self.url,
                api_headers=self.api_headers
            )

        else:
            self.url = "https://testwx.baijiayun.com"+self.analysis_url(api_url)
            self.data = self.analysis_data(api_data)  # 字典格式
            self.data_1 = json.dumps(self.data)  # json字符串
            self.api_headers = headers

            response = self.get_function(
                method=api_function,
                api_url=self.url,
                api_headers=self.api_headers,
                api_data=self.data
            )




        # response1 = json.loads(response[1])  # 解析返回值
        self.analysis_response(api_correlation, response)
        return response



    def analysis_response(self,correlation,response):
        '''
        于解析返回值中的数据，将这些数据存入关联字典中以供使用
        :param correlation: 关联参数
        :param response: 接口返回值
        :return:
        '''

        if correlation != "":
            #处理关联数据，存在列表中
            correlation = correlation.replace(" ","").replace("\n","").replace("\r","").split(";")
            #分解关联数据
            for i in range(len(correlation)):
                parms = correlation[i].split("=")
                if len(parms)==2:
                    if parms[1] == "" or not re.search(r"^\[",parms[1]) or not re.search(r"\]$",parms[1]):
                        print("correlation:"+"填写错误")
                        continue
                    response = response.json()
                    vaule = response

                    #继续处理correlation
                    a = parms[1][1:-1].split("][")
                    for j in a:
                        try:
                            temp = vaule[int(j)]
                        except:
                            try:
                                temp = vaule[j]
                            except:
                                pass
                        vaule = temp
                    self.correlationDict[parms[0]] = vaule

        return self.correlationDict

    def analysis_data(self,api_data):
        '''
        处理关联参数
        :return:
        '''
        #字符串转换成字典
        # print("---------------开始啦---------------")
        # print(api_data,type(api_data))
        dic_api_data = eval(api_data)
        # print("---------------结束了--------------------------------------------------------------")
        # print(dic_api_data,type(dic_api_data))
        #2. 利用列表迭代字典，查找value=None项，并删掉
        for key in list(dic_api_data.keys()):
            if dic_api_data[key] == None:
                del dic_api_data[key]

            # 遍历管理字典
        for key, value in self.correlationDict.items():
            # 遍历请求数据
            for akey, avalue in dic_api_data.items():
                # 如果关联字典中的key在请求数据的value中存在
                # 有些avalue是整型，而key是字符串，导致不能迭代，所以用try处理
                try:
                    if key in avalue:
                        # 将所有符合key的值都替换value
                        dic_api_data[akey] = avalue.replace(key, str(value))
                except:
                    pass
        return dic_api_data

    def analysis_url(self,api_url):
        '''
        解析URL中的关联数据
        :param URL:
        :return:
        '''
        for key in self.correlationDict.keys():
            if key in api_url:

                api_url = str(api_url).replace(key,str(self.correlationDict[key]))

        api_url = api_url.replace(" ", "")
        return api_url
    # def analysis_check(self,api_check,response):
    #     '''
    #     解析检查点中的关联数据
    #     :param api_check:
    #     :return:
    #     '''
    #     flag = ""
    #     if api_check != "":
    #         api_check = str(api_check).replace(" ","").replace("\n","").replace("\r","").split(";")
    #         #分解关联数据
    #         for i in len(api_check):
    #             if "=" in api_check[i]:




a = requestApi()

for i in a.data:
    # print(a.correlationDict)
    # b = a.api_requests(i[0], i[3], i[4], i[6], i[12])
    # print("用例" + i[0])
    try:
        # print(a.data)
        b=a.api_requests(i[0],i[3],i[4],i[6],i[12])
        if b.json()["code"] ==200:
            print("用例执行成功,用例编号："+i[0])

    except Exception as e:
        import traceback
        traceback.print_exc()
        print("用例执行失败" + i[0])

