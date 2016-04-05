__author__ = 'sherry'

# names = ['zhangshan','lisi','wangwu','sunliu']
#
# numbers = ['2133','3354','3454','5454']
#
# print numbers[names.index('zhangshan')]
#
# phonebook = {'zhangshan':'2133','lisi':'3354','wangwu':'3454','sunliu':'5454'}

people = {
    'zhangshan': {
        'phone': '2133',
        'addr': 'foo drive 23'
    },
    'lisi': {
        'phone': '3354',
        'addr': 'bar street 42'
    },
    'wangwu': {
        'phone': '3453',
        'addr': 'baz avenue 90'
    }
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = raw_input('Enter name : ')

request = raw_input('phone number(p) or address(a)?')

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

if name in people:
    print "%s's %s is %s. " % (name, labels[key], people[name][key])
