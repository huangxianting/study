__author__ = 'sherry'

#coding:utf-8

import random
import string

numbers = [str(r) for r in range(0, 10) * 2]
email_hosts = ['@qq.com', '@163.com', '@126.com', '@189.com', '@hotmail']
area_code = ['010','021','0733','022','0311']

chars = string.lowercase + ''.join(numbers)


def get_random_mobliephone(size=11):
    max_size = len(numbers)
    if size > max_size:
        size = max_size
    return random.sample(numbers, size)

def get_random_workphone(size=8, start = '', ends=(2,6)):
    max_size = len(numbers)
    if size > max_size:
        size = max_size
    start = random.sample(area_code, 1)
    return start  + ['-']  + random.sample(numbers, size) + ['*'] + random.sample(numbers, ends)


def get_random_email(size=5, ends=''):
    if not ends:
        ends = random.sample(email_hosts, 1)
    return random.sample(chars, size) + ends


print ''.join(get_random_email())
print ''.join(get_random_mobliephone())
print ''.join(get_random_workphone())