__author__ = 'sherry'

import os
import shutil
import codecs

fb = open('/Users/sherry/Documents/My Father.txt','r')

file = fb.read()
alist = file.split()

print file
print len(alist)
print alist

fb.close()
