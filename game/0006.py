# coding:utf-8
# 统计目录里的代码行数
import os

__author__ = 'sherry'


def find_file(path='/Users/sherry/PycharmProjects/study_selenium/'):
    file_list = os.listdir(path)
    for file_name in file_list:
        file_type = os.path.splitext(file_name)[-1]
        if file_type == '.py':
            yield os.path.join(path, file_name)


def new_py():
    fb = []
    count_annotation = 0
    for file_name in find_file():
        py = open(file_name, 'r')
        x = py.readlines()
        for line in x:
            if line.startswith("#"):
                count_annotation += 1
        fb.extend(x)
    # print '你的代码总行数为：%s' % len(fb)
    # print '其中空行有：%s' %fb.count('\n')
    # print '其中注释有：%s' %count_annotation
    return fb, count_annotation


def count_py():
    fb, count_annotation = new_py()
    print '你的代码总行数为：%s' % len(fb)
    print '其中空行有：%s' %fb.count('\n')
    print '其中注释有：%s' %count_annotation

count_py()
#
# new_py()

