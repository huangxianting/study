# coding:utf-8
from collections import OrderedDict

import json
import requests
import os
from utils.get_date import this_week, this_week_kpi, last_week_kpi
from utils.get_date import last_week

cookies = {
    'JSESSIONID': 'fcdcd70e-c428-4ae7-8adb-db521a99cfb8',
    '_id': '-29384'
}

headers = {'Content-type': 'application/json'}


def get_event_data(types=16):
    page = 1
    size = 100
    count = 0
    url = 'http://dev.jihui.in/api/event'
    payload = {
        'query': {
            'operBys': [-29384],
            'createAts': last_week(),
            # 'contactTypes': [1]
            'types': [types]
        },
    }

    target_resume_count = set()
    while 1:
        print('current page:%s size:%s types:%s' % (page, size, types))
        payload['page'] = page
        payload['size'] = size
        resp = requests.post(url, headers=headers, cookies=cookies, data=json.dumps(payload))
        data = json.loads(resp.content)
        for r in data.get('_body', []):
            resume = r.get('targetResume')
            for user in resume:
                target_resume_count.add(user['id'])
        pagination = data.get('_meta', {}).get('pagination')
        total_page = pagination.get('totalPages')
        # print json.dumps(json.loads(resp.content), indent=4)
        count += resp.text.count('"type":%s' % types)
        if page == total_page:
            break
        else:
            page += 1
    print(count, target_resume_count)
    return count, len(target_resume_count)


def add_kpi(item_id):
    url = 'http://dev.jihui.in/api/stats/item/add'
    data = {
        'itemId': item_id,
        'isKpi': False
    }
    resp = requests.post(url, headers=headers, cookies=cookies, data=json.dumps(data))
    print('set item:[%s] status:[%s]' % (item_id, resp.status_code))


def get_kpi(item_ids):
    start_day, end_day = last_week_kpi()
    url = 'http://dev.jihui.in/api/stats/view/node/summary'
    params = {
        'startAt': start_day,
        'endAt': end_day
    }
    resp = requests.get(url, params=params, headers=headers, cookies=cookies)
    print resp.elapsed
    data = json.loads(resp.content)
    res = OrderedDict()
    for r in data.get('_body'):
        item_id = r['itemId']
        if item_id in item_ids:
            value = r.get('completedValue', 0)
            print('hit item_id:[%s] of value:[%s]' % (item_id, value))
            res[item_id] = value
    return res




if __name__ == '__main__':
    total_count, target_resume_count = get_event_data(16)
    print('target resume user count:%s' % target_resume_count)
    item_ids = [335, 345]
    for r in item_ids:
        add_kpi(r)
    kpi_count = get_kpi(item_ids)
    print(kpi_count.get(335) == target_resume_count)
    print(kpi_count.get(345) == total_count)









    # CANDIDATE_NODE_RECRUIT_CALL_count = resp.text.count('"type":16')
    #
    # #  #招聘电话的候选人数量
    # # targetResume
    #
    # print CANDIDATE_NODE_RECRUIT_CALL
