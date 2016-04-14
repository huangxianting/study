#coding:utf-8
import random
import math

__author__ = 'sherry'

# # 练习1
# for i in range(1, 5):
#     for k in range(1, 5):
#         for j in range(1, 5):
#             if (i != k) and (i != j) and (j != k):
#                 print i,j,k

# # 练习2
# i  = int(raw_input('请输入当月利润：'))
# if i <= 1e5:
#    reward = i * 0.1
# elif 1e5 < i <= 2e5:
#     reward = 1e4 + (2e5 - i) * 0.075
# elif 2e5 < i <= 4e5:
#     reward = (i - 2e5) * 0.05
# elif 4e5 < i <= 6e5:
#     reward = (i - 4e5) * 0.03
# elif 6e5 < i <= 10e5:
#     reward = (i - 10e5) * 0.015
# elif i > 10e5:
#     reward = (10e5 - i) * 0.01
# print reward

# 练习3
#
# i = 1
# for i in range(10000):
#     x = i + 100
#     y = x + 268
#
#     if math.sqrt(x) == int(math.sqrt(x)) and math.sqrt(y) == int(math.sqrt(y)):
#         print i

# f1 = 1
# f2 = 1
# for i in range(1, 21):
#     print '%s %s' %(f1,f2)
#     if (i % 2) == 0:
#         print ''
#     f1 = f1 + f2
#     f2 = f1 + f2
#

class Bird:
    song = 'Squaawk!'

    def sing(self):
        print self.song


bird = Bird()
bird.sing()
