# coding=utf-8
__author__ = 'sherry'

import random

secret = random.randint(1,10)
i = 0
for i in range(3):
    # temp = raw_input('猜猜我心里想的数字，有惊喜喔：')
    # if temp.isdigit() == 0:
    #     print '请输入正确的数字。'
    #     continue
    # else:
    #     guess = int(temp)
    try:
        temp = raw_input('猜猜我心里想的数字，有惊喜喔：')
        guess = int(temp)
    except ValueError:
        print '请输入正确的数字。'


    if guess == secret:
        print '恭喜你，猜对啦！不过没有奖励喔。'
        break
    elif guess > secret:
        print '你想的数字可能大了喔，试着输入更小的数字吧。'
        continue
    elif guess < secret:
        print '你想的数字可能小了喔，试着输入更大的数字吧。'
        continue


print '游戏结束！'
