from cfg import headers
import requests
import os
#D:/测试文件/教育类图片/401f8822a181902b69955f8e1a2983c9.jpeg

# 图片上传
def updateImage(imagpath,imagname):

    request_url = "https://testwx.baijiayun.com/api/public/img"
    fl = open(imagpath,"rb")
    # 字段名files 以及类型和application/octet-stream 和抓取到的接口一致
    files = {'file': (imagname, fl, 'image/jpeg', {'Expires': '0'})}
    repeson = requests.post(request_url, headers=headers, files=files).json()

    return repeson
# nowpath = os.path.dirname(__file__)
# imagpath = nowpath +"/photo/600.jpg"
# imagname = "600.jpg"
# a= updateImage(imagpath,imagname)
# print(a)


# fl = open(r"D:/测试文件/文库/添加检查点.docx",'rb')
# request_url = "https://testwx.baijiayun.com/api/public/file"
# files_obj = {"file":fl}
# files  = {'file': ("11-20前台.xlsx", fl, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",{'Expires': '0'})}  #字段名files 以及类型和application/octet-stream 和抓取到的接口一致
# files = {"file":open(r"D:/测试文件/文库/11-20前台.xlsx","rb")}
#
# files = {
#     'file':open(r"D:/测试文件/文库/11-20前台.xlsx","rb"),
#     'Content-Disposition': 'form-data',
#     'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
#     'filename':'11-20前台.xlsx'
#     }
# r3 = requests.post(request_url, headers=headers, files=files_obj)
#
# print(r3.json())
#
#
#
# url = "https://b62327424.at.baijiayun.com/"
# Partner_ID="62327424"
# Partner_Key ="PPS/Fe2xWDd4FAJO3Ti1nk3vzeniOAnBbGAyfhWmFSYvZ5ivmTx5dEe5qFcscidzY5WGamUSt9PtYa6Zx4txwM9wGp6V1uJ4vq1RuIkfDjJcXOV/AH1zXTKwRVstYdXA"
