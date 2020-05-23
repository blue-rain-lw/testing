import requests
import random
payload = {
    "mobile":"admin",
    "password":"123456"
}
r = requests.post("https://testwx.baijiayun.com/api/adminUser/login",data=payload)
cookie = r.json()["data"]["remember_token"]
headers = {"authorization":f"Bearer  {cookie}"}

num = "".join(str(random.choice(range(10))) for _ in range(10))
mobile = "{}{}".format("1",num)
