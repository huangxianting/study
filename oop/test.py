__author__ = 'Xin'


# def fibs(num):
#     result = [0, 1]
#     for i in range(num):
#         result.append(result[-2] + result[-1])
#     return result
#
# x = raw_input('Enter number:')
# print x, type(x)
# print type(int(x))
# print fibs(int(x))


# import math
#
# x = 1
# y = math.sqrt
# print callable(y)

# def hello(name):
#     return 'hello.' + name + '!'
#
# print hello('sherry')


# def func():
#     global x
#     print 'x is', x
#     x = 2
#     print 'changed local x to', x
#
#
# x = 50
# func()
#
# print 'value of x is', x
#
#
# def say(message, times=1):
#     print message * times
#
#
# say('hello')
#
# say('sherry', 4)

# def func(a, b=5, c=10):
#     print 'a is', a, 'and b is', b, 'and c is', c
#
#
# func(3, 6)
# func(3, 6, 9)
# func(3, c=13)
# func(c=34, a=2, b=23)

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return n * f(n - 1)
#
# print f(3)


def f(n):
    i = 1
    x = 0
    y = 0
    while i in range(1, n):
        print(i)
        if i % 2 == 0:
            x = x + i
        else:
            y = y + i
        i += 1
    return x, y


print f(100)
