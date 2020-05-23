import requests
from wangxiao.wangxiao import quanju
import addCourse



#添加课程章节
def add_chapter():
    courseid = addCourse.list_course()
    payload3 = {
        "course_basis_id":courseid,
        "course_type": 2,
        "parent_id": 0,
        "sort": 0,
        "title": "第一章"
    }
    addchapter = requests.post("https://testwx.baijiayun.com/api/course/chapter",data=payload3,headers=quanju.headers)
    chapterID = addchapter.json()["data"]["id"]
    return chapterID

add_chapter()
#创建课时
def add_parent():
    courseid = addCourse.list_course()
    payload3 = {
    "advance_time": 0,
    "assist_ids": "",
    "course_basis_id": courseid,
    "course_content": "",
    "course_type": 2,
    "end_play": "2020-04-15 07:00",
    "file_name": "",
    "file_url": "",
    "is_playback": 1,
    "is_try_see": 0,
    "parent_id": add_chapter(),
    "room_video_id": "",
    "sort": 0,
    "start_play": "2020-04-14 00:00",
    "teacher_id": "22",
    "teacher_ids": "",
    "title": "第二课时"
}
    addparent = requests.post("https://testwx.baijiayun.com/api/course/chapter", data=payload3, headers=quanju.headers)
    print(addparent.json())

add_parent()