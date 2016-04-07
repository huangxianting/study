__author__ = 'Xin'


class Person(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def say_hi(self, name):
        print('%s say hi to %s' % (self.name, name))


class Boy(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, 'boy', age)


class Girl(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, 'girl', age)


xin = Girl('xin', 26)
xin.say_hi('zoe')
print xin.age
print xin.sex