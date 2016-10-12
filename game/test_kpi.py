#coding:utf-8

import json
import requests
import os
from utils.get_date import this_week
from utils.get_date import last_week

if __name__ == '__main__':
    url = 'http://dev.jihui.in/api/event'
    pqyload = {
        'query': {
            'operBys': [-29384],
            'createAts': last_week(),
            # 'contactTypes': [1]
            'types': [16]
        },
    }
    cookies = {
        'JSESSIONID': 'fcdcd70e-c428-4ae7-8adb-db521a99cfb8',
        '_id': '-29384'
    }


page = 1
while 1:
    headers = {'Content-type': 'application/json'}
    resp = requests.post(url, headers=headers, cookies=cookies, data=json.dumps(pqyload))
    print json.dumps(json.loads(resp.content), indent=4)
    data.get('pagination', {}).get('totalPages', 1)
    if page == totalPages:
            break
    else:
        page += 1






# CANDIDATE_NODE_RECRUIT_CALL_count = resp.text.count('"type":16')
#
# #  #招聘电话的候选人数量
# # targetResume
#
# print CANDIDATE_NODE_RECRUIT_CALL