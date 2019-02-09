#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from my_context import *

class Cat(Context):
    def __init__(self, name=''):
        super(Cat, self).__init__()
        self.name = name

    def speak(self):
        self.greet()

    def greet(self):
        for c in reversed(self.layers):
            if 'base' == c:
                self.greet_base()
                break
            elif 'jp' == c:
                self.greet_jp()
                break
            else:
                pass

    def greet_base(self):
        print("base greet cat")

    def greet_jp(self):
        print("mea")

class Person(Context):
    def __init__(self, name=''):
        super(Person, self).__init__()
        self.name = name

    def speak(self):
        self.greet()
        c = Cat()
        c.greet()

    def func(self):
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    def greet(self):
        for c in reversed(self.layers):
            if 'base' == c:
                self.greet_base()
                break
            elif 'jp' == c:
                self.greet_jp()
                break
            else:
                pass
    def greet_base(self):
        print("base greet")

    def greet_jp(self):
        print("こんにちは")


class ExPerson(Person):
    def __init__(self, name=''):
        super(ExPerson, self).__init__(name)
        self.name = name
        super(ExPerson, self).func()
        print super(ExPerson, self).__class__.__name__

class ExExPerson(ExPerson):
    def __init__(self, name=''):
        super(ExExPerson, self).__init__(name)
        self.name = name
        super(ExExPerson, self).func()
        print super(ExExPerson, self).__class__.__name__

if __name__ == '__main__':
    p1 = Person("Yuta")
    p2 = Person("John")
    p1.func()
    p3 = ExPerson('J')
    p4 = ExExPerson('J')
    # for key, value in c.__dict__.items():
    #     print(key, ':', value)
    # c = Cat("Nyan")
    # p1.speak()
    # p2.speak()
    # c.speak()
    # p1.activate('jp')
    # p1.speak()
    # p2.speak()
    # c.speak()
