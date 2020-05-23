import re
import requests
from add_teacher import list_teacher

list_teacher()
response = list_teacher()

def analysis_response(correlation: str, response: dict) -> dict:
    '''
    用于解析返回值中的数据，将这些数据存入关联字典中以供使用
    :param api_no       : 接口编号
    :param api_name     : 接口名称
    :param correlation  : 关联字典
    :param response     : 接口返回值
    :return:
    '''
    # 如果关联数据不为空
    if correlation != '':
        # 1.处理关联数据(存到列表中)
        correlation = correlation.replace('\n', '').replace('\r', '').split(';')

        # 2.分解关联数据
        for j in range(len(correlation)):
            param = correlation[j].split('=')

            # 3.判断处理后的关联列表长度为2时
            if len(param) == 2:
                # if param[1] == '' or not re.search(r'^\[', param[1]) or not re.search(r'\]$', param[1]):
                #     self.log.error(
                #         api_no + ' ' + api_name + ' analysis_response:关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                #     continue

                # 4.返回结果赋值
                value = response

                # 5.继续处理correlation
                a = param[1][1:-1].split('][')
                print(a)
                # 6.循环遍历列表的键
                for key in a:
                    try:
                        temp = value[int(key)]
                    except:
                        try:
                            temp = value[key]
                        except:
                            break
                    value = temp

                # correlationDict[param[0]] = value
    return print(value,param[0])

a = "${teacher_id}=[data][list][0][id]"
analysis_response(a,response)



correlationDict = {
    '${room_id_default}':21,
    '${room_id_default1}':23
}
api_data = '''{
 'room_id':'${room_id_default},${room_id_default1}',
}'''
def analysis_data(api_data: str) -> dict:
    '''
    用于解析关联数据，将需要关联的字段存到关联字典中
    :param api_data : 接口请求数据
    :return:
    '''
    # 1.请求数据：字符串转字典
    dic_api_data = eval(api_data)

    # 2. 利用列表迭代字典，查找value=None项，并删掉
    # 为了满足部分同学复制粘贴所有数据，但是有些参数可以不传，既可以不传也可以填None，填None这里会自动的去除掉这个参数
    for key in list(dic_api_data.keys()):
        if dic_api_data[key] == None:
            del dic_api_data[key]

    # 2.循环遍历测试数据
    '''
        20181022 xjy重写解析参数关联度的方法：
        目的：用于解析一个key对应的value有多个关联值的情况
        例如：
        {
            'key' : 'value1,value2' # 这里的value1和value2都是关联数据需要替换
        }
    '''
    # 遍历管理字典
    for key, value in correlationDict.items():
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

a = analysis_data(api_data)
print(a)
def get_url(url):
    with requests.Session() as s:
        r = s.post(url, params=r_data, headers=headers)
        ORGSESSID = r.cookies.get_dict()['ORGSESSID']
        self.cookie = 'ORGSESSID=' + ORGSESSID
        headers = {
            'Cookie': self.cookie
        }
        self.log.debug('登录,cookie: ' + self.cookie)