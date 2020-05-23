import requests

headers = {
    "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3Rlc3R3eC5iYWlqaWF5dW4uY29tL2FwaS9hZG1pblVzZXIvbG9naW4iLCJpYXQiOjE1ODYyMjcyOTUsImV4cCI6MTU4NjUyOTY5NSwibmJmIjoxNTg2MjI3Mjk1LCJqdGkiOiJPMXNBb2FmWGVjY1c4TWhZIiwic3ViIjoxLCJwcnYiOiJlNTM4NDI5ODM0NjJiZDg5NTJhZTU5MjM2MzdhY2EwZTk2YjI1OThjIn0.P_5k8644eVVnunMTUeu1nKqj3JwjgWZYD9U_8wSosOg"
 }
# payload = {
#     "mobile":"17622225565",
#     "nickname":"xingming"
# }
#
# r = requests.post("https://testwx.baijiayun.com/api/user",data=payload,headers=headers)
# print(r.text)
#


payload1 = {
        "course_type":2,
        "course_classify_id":"15",
        "title":"课程标题",
        "display_style":1,
        "sales_base":12,
        "sale_type":0,
        "browse_base":123,
        "teacher_ids":'''
        [{“teacher_id”:”12”, 
        “teacher_name”:”我是讲师”}]''',
        "is_divide_group":0,
        "is_go_to_study":0,
        "advance_time":10
    }
#大班课
def add_course(title):
    payload2 = {
        "address": "",
        "advance_time": 0,
        "assist_teacher_ids": "[]",
        "basis_ids": "[]",
        "browse_base": 0,
        "city_id": 0,
        "course_attr": '''[{"attr_id":4,"attr_val_id":7},{"attr_id":4,"attr_val_id":8},{"attr_id":3,"attr_val_id":6},{"attr_id":5,"attr_val_id":12}]''',
        "course_classify_id": 15,
        "course_details": "<p>课程详情</p>",
        "course_service_id": "4,5",
        "course_type": 2,
        "cover_img": "",
        "display_style": 0,
        "district_id": 0,
        "group_num": 0,
        "is_divide_group": 0,
        "is_go_to_study": "1",
        "is_materials": 0,
        "off_stock": "",
        "price": 0,
        "province_id": 0,
        "sale_type": 0,
        "sales_base": 123,
        "shelf_time": "",
        "status": "1",
        "stock": 0,
        "teacher_ids": '''[{"teacher_id":22,"teacher_name":"好讲师"},{"teacher_id":21,"teacher_name":"测试排课讲师"}]''',
        "title": {title},
        "underlined_price": 0
    }
    r1 = requests.post("https://testwx.baijiayun.com/api/course/basis",data=payload2,headers=headers)


    return    print(r1.text)
#add_course("自动添加的课程")
# 大班课
payload2 = {
    "address": "",
    "advance_time": 0,
    "assist_teacher_ids": "[]",
    "basis_ids": "[]",
    "browse_base": 0,
    "city_id": 0,
    "course_attr": '''[{"attr_id":4,"attr_val_id":7},{"attr_id":4,"attr_val_id":8},{"attr_id":3,"attr_val_id":6},{"attr_id":5,"attr_val_id":12}]''',
    "course_classify_id": 15,
    "course_details": "<p>课程详情</p>",
    "course_service_id": "4,5",
    "course_type": 2,
    "cover_img": "",
    "display_style": 0,
    "district_id": 0,
    "group_num": 0,
    "is_divide_group": 0,
    "is_go_to_study": "1",
    "is_materials": 0,
    "off_stock": "",
    "price": 0,
    "province_id": 0,
    "sale_type": 0,
    "sales_base": 123,
    "shelf_time": "",
    "status": "1",
    "stock": 0,
    "teacher_ids": '''[{"teacher_id":22,"teacher_name":"好讲师"},{"teacher_id":21,"teacher_name":"测试排课讲师"}]''',
    "title": "课程名称",
    "underlined_price": 0
}

#添加课程章节
payload3 = {
    "course_basis_id": 153,
    "course_type": 2,
    "parent_id": 0,
    "sort": 0,
    "title": "第一章"
}
# r = requests.post("https://testwx.baijiayun.com/api/course/chapter",data=payload3,headers = headers)
# print(r.text)

#创建课时
payload4 = {
    "advance_time": 0,
    "assist_ids": "",
    "course_basis_id": "153",
    "course_content": "",
    "course_type": 2,
    "end_play": "2020-04-10 07:00",
    "file_name": "",
    "file_url": "",
    "is_playback": 1,
    "is_try_see": 0,
    "parent_id": "368",
    "room_video_id": "",
    "sort": 0,
    "start_play": "2020-04-10 00:00",
    "teacher_id": "22",
    "teacher_ids": "",
    "title": "第二课时"
}
import pprint
# r5 = requests.post("https://testwx.baijiayun.com/api/course/chapter",data=payload4,headers = headers)
# print(r5.text)
r5 = requests.get("https://testwx.baijiayun.com/api/teacher")
r5.encoding = "utf-8"
print(r5.text)


