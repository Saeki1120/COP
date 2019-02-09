#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Context(object):
    layers = ['base']
    def __init__(cls):
        cls.init_layer()

    @classmethod
    def init_layer(cls):
        if not hasattr(cls, 'layers'):
            cls.layers = ['base']

    @classmethod
    def activate(cls, layer):
        if not layer == 'base':
            cls.layers.append(layer)

    @classmethod
    def deactivate(cls, layer):
        if not layer == 'base':
            cls.layers.remove(layer)

    def change(self):
        pass

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

if __name__ == '__main__':
    p1 = Person("Yuta")
    p2 = Person("John")
    p1.func()
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
