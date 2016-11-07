__author__ = 'Xin'
#coding:utf-8

import json
import requests

url = 'http://dev.jihui.in/api/login'

headers = {'content-type': 'application/json'}

data = {'email' : 'alicebao','password' : "123456"}

r = requests.post(url, data = json.dumps(data), headers = headers)

payload = {
    'page': 1,
    'size': 10,
    'sort':'',
    'query': {
        'type': [1, 2, 3]
    }

}

s = requests.post('http://dev.jihui.in/api/v2/search/resume_v2', data = json.dumps(payload), headers = headers)

print r.status_code
print json.dumps(json.loads(s.content), indent=5)