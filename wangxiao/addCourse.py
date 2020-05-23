import requests
from wangxiao.wangxiao import quanju
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
        "is_materials": 1,
        "off_stock": "",
        "price": 0,
        "province_id": 0,
        "sale_type": 0,
        "sales_base": 123,
        "shelf_time": "",
        "status": "1",
        "stock": 0,
        "teacher_ids": '''[{"teacher_id":22,"teacher_name":"好讲师"}]''',
        "title": {title},
        "underlined_price": 0
    }
    addcourse = requests.post("http://testwx.baijiayun.com/api/course/basis",data=payload2,headers=quanju.headers)
    courseid = addcourse.json()["data"]["id"]
    return courseid
#add_course("新的大班课")

def list_course():
    payload = {
        "course_classify_id": 0,
        "course_type": "",
        "finish_created_at": "",
        "keywords": "",
        "keywords_type": "title",
        "limit": 10,
        "page": 1,
        "start_created_at": "",
        "status": "",
        "teacher_id": ""
    }
    listcourse = requests.post("https://testwx.baijiayun.com/api/course/basis/index",data=payload,headers=quanju.headers)
    courseID = listcourse.json()["data"]["list"][0]["id"]
    return courseID
list_course()
add_course("需要收货地址")