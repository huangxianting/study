

__author__ = 'sherry'

_metaclass_ = type


class Person:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self, name

    def greet(self):
        print "Hello, world!I'm %s" % self.name


huhu = Person()

huhu.name = 'sherry'

huhu.greet()
