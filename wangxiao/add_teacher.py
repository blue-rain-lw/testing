import requests
from cfg import headers,mobile
# from file_phont import updateImage
#img = file_phont.read_directory(r"C:\Users\Administrator\HelloWorld\wangxiao\wangxiao\phont")[0]
# def add_teacher(people_photo,herd_photo):
#     avatar = updateImage("D:/测试文件/教育类图片/401f8822a181902b69955f8e1a2983c9.jpeg", "401f8822a181902b69955f8e1a2983c9.jpeg")
#     payload = {
#         "attr": [],
#         "avatar": herd_photo,
#         "introduction": "讲师简介z这个是讲师简介",
#         "marketing_language":"这个是讲师的一句话营销语",
#         "photo":people_photo,
#         "mobile": 17671156789,
#         "real_name": "讲师名称",
#         "teacher_attr": "[]"
#     }
#     addteacher = requests.post("https://testwx.baijiayun.com/api/teacher",data=payload,headers = headers)
#     return print(addteacher.json())

def list_teacher():
    teacherlist = requests.get("https://testwx.baijiayun.com/api/teacher",headers = headers).json()
    return teacherlist

# def verify_teacher():
#     tecaherid = list_teacher()["data"]["list"][0]["id"]
#     payload = {
#        "approval_status":2,
#         "approval_failed_message":""
#     }
#     verifyteacher = requests.put(f"https://testwx.baijiayun.com/api/teacher/verify/{tecaherid}",data=payload,headers = headers).json()
#     return verifyteacher
#
# def show_teacher():
#     tecaherid = list_teacher()["data"]["list"][0]["id"]
#     is_show = 1
#     showteacher = requests.get(f"https://testwx.baijiayun.com/api/teacher/verify/{tecaherid}/{is_show}",headers = headers).json()
#     return showteacher
#
# def perfectteacher():
#     add_teacher("{}{}".format("讲师",mobile),mobile)
#     list_teacher()
#     verify_teacher()
#     show_teacher()

list_teacher()


