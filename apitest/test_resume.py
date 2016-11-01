__author__ = 'sherry'
#coding = utf-8
import requests
import json


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Content-Type': 'application/json;charset=UTF-8',
    'cookie': 'JSESSIONID=6da3450a-9826-4a84-8e32-454747189d7a; _id=17',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'X-RequestedWith': 'XMLHttpRequest'
}

# payload = {
#     'srcType': '2',
#     'srcId': '227663'
# }
# s = requests.post(url = 'http://dev.jihui.in/api/access', headers = headers, data = json.dumps(payload))
# print s.status_code

for i in range(1000, 500 + 1000):
    payload = {
    'srcType': '2',
    'srcId': i
            }
    # resume = requests.get(url = 'http://dev.jihui.in/api/resume/%s?loadding=true' % i, headers = headers)
    access = requests.post(url = 'http://dev.jihui.in/api/access', headers = headers, data = json.dumps(payload))
    print access.text


# payload = {
#     'query':
#     {
#         'poerBys': '[88]'
#      },
#         'page': '1',
#         'size': '10'
# }
#
# event = requests.post('http://dev.jihui.in/api/event', headers = headers, cookies = cookie, data = json.dumps(payload))
#
# print event.text

