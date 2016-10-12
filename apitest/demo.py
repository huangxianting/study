# encoding: utf-8

__author__ = 'Xin'

import json
import requests

if __name__ == '__main__':

    # url = 'http://irp.higgspro.com/api-docs/api/v1/user'
    # resp = requests.get(url, auth=('higgs', 'higgs'))
    # data = json.loads(resp.content)
    # apis = data.get('apis')
    # print apis[0]

    url = 'http://irp.higgspro.com/api/v1/user/auth/token'
    data = {'username': '', 'password': ''}
    resp = requests.post(url, data=data)
    print resp
    print resp.content