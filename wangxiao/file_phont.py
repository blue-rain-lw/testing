from wangxiao.cfg import headers
import requests

#D:/测试文件/教育类图片/401f8822a181902b69955f8e1a2983c9.jpeg

#图片上传
def updateImage(imagpath,imagname):
    request_url = "https://testwx.baijiayun.com/api/public/img"
    fl = open(imagpath,"rb")
    files = {'file': (imagname, fl, 'image/jpeg', {'Expires': '0'})}  #字段名files 以及类型和application/octet-stream 和抓取到的接口一致
    r2 = requests.post(request_url, headers=headers , files=files).json()
    imageurl = r2["data"]["path"]
    return imageurl


#文件上传
#request_url = "https://testwx.baijiayun.com/api/public/file"
#files  = {'file': ("11-20前台.xlsx", fl, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",{'Expires': '0'})}  #字段名files 以及类型和application/octet-stream 和抓取到的接口一致
#files = {"file":open(r"D:/测试文件/文库/11-20前台.xlsx","rb")}

# files = {
#     'file':open(r"D:/测试文件/文库/11-20前台.xlsx","rb"),   # => 用name指定文件
#     'Content-Disposition': 'form-data',
#     'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
#     'filename':'11-20前台.xlsx'
#     }
# r3 = requests.post(request_url, headers=headers, files=files)
#
# print(r3.json())