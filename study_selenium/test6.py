__author__ = 'sherry'

# greeting = 'china'
#
# print greeting[2]
# print greeting[-1]
#
# fourth = raw_input('year:')[3]
#
# print fourth
#
# months = [
#     'January',
#     'February',
#     'March',
#     'April',
#     'May',
#     'June',
#     'July',
#     'August',
#     'September',
#     'October',
#     'November',
#     'December'
#     ]
#
# endings = ['st','nd','rd']+ 17*['th']\
#            +['st','nd','rd']+ 7*['th']\
#            +['st']
#
# year = raw_input('year:')
# month = raw_input('month:')
# day = raw_input('day(1-31):')
#
# month_number = int(month)
# day_number = int(day)
#
# month_name = months[month_number-1]
# ordinal = day + endings[day_number - 1]
#
# print month_name + ',' + ordinal + ',' + year
#
# print  endings


# numbers = [0,1,2,3,4,5,6,7,8,9,10]
#
# print numbers[0:10:5]

# url = raw_input('Please enter the URL:')
#
# domain = url[11:23]
#
# print 'Domain name:' + domain
#
# print [1,2,3] + [4,5,6]

# sen = raw_input(u'Sentence : ')
#
# screen_width = 80
#
# text_width = len(sen)
#
# box_width = text_width
#
# left_margin = (screen_width - box_width) // 2
#
# print box_width
# print left_margin
#
# # print ' ' * left_margin + '+' + '-' * (box_width + 2) + '+'
# #
# # print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
# #
# # print ' ' * left_margin + '| ' + sen + ' |'
# #
# # print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
# #
# # print ' ' * left_margin + '+' + '-' * (box_width + 2) + '+'
#
# print '+' + '-' * (box_width + 2) + '+'
#
# print '| ' + ' ' * text_width + ' |'
#
# print '| ' + sen + ' |'
#
# print '| ' + ' ' * text_width + ' |'
#
# print '+' + '-' * (box_width + 2) + '+'

# x = 1
#
# while x <= 100:
#     print x
#     x += 1

# name = 'hh'
#
# while not name:
#     name = raw_input('please enter your name:')
# print  'hello.%s!' %name
#

# for number in range(1,101):
#     print number

# d = {'x':1,'y':2,'z':3}
# for key, v in d.items():
#     print key,'corrsponds to', v
#
# from math import sqrt
#
# for n in range(99,0,-1):
#     root = sqrt(n)
#     if root == int(root):
#         print n, root
#         continue

index = 0
while index < 3:
    index += 1
    s = raw_input('enter sth:')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print 'Input is of sufficient length!'