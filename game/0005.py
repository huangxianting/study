# coding:utf-8
__author__ = 'sherry'

import os
from PIL import Image

def find_file(path = '/Users/sherry/Downloads/images/'):
    file_list = os.listdir(path)
    for file_name in file_list:
        file_split = os.path.splitext(file_name)
        file_type = file_split[-1]
        img_type = ['.bmp', '.jpeg', '.gif', '.psd', '.png', '.jpg']

        if file_type in img_type:
            yield os.path.join(path, file_name)

def change_size():
    for file_name in find_file():
        file_prev, file_ends = os.path.split(file_name)
        file_name2, file_type = os.path.splitext(file_ends)
        img = Image.open(file_name)
        new = img.resize((120, 120), Image.ANTIALIAS)
        new_file_name = os.path.join(file_prev, (file_name2 + '_120*120' + file_type))
        # new_file_name = '%s%s_small%s' % (file_prev, file_name2, file_type)
        # print new_file_name
        new.save(new_file_name)

change_size()