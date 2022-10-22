from datetime import date
from wsgiref.util import request_uri
import requests
url='https://fanyi.baidu.com/sug'
s=input("请输入查找的单词")
dat={
    "kw":s
}
date=dat
resp=requests.post(url,date)
print(resp.json())