#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crospy import *

class Person(CPy):
    def __init__(self, name=''):
        super(Person, self).__init__()
        self.name = name

    def my_name(self):
        print(self.name)

    @cpybase
    def greet(self):
        print("person base greet")

    @cpybase
    def apologize(self):
        print("person base apologize")

@cpylayer(Person, 'jp', 'greet')
def greet(self):
    print("こんにちは")

@cpylayer(Person, 'jp', 'apologize')
def greet(self):
    print("ごめんなさい")


class Cat(CPy):
    def __init__(self, name=''):
        super(Cat, self).__init__()
        self.name = name

    def my_name(self):
        print(self.name)

    @cpybase
    def greet(self):
        print("cat base greet")

    @cpybase
    def fawn_on(self):
        print("cat base fawn_on")

@cpylayer(Cat, 'jp', 'greet')
def greet(self):
    print("にゃー")

@cpylayer(Cat, 'jp', 'fawn_on')
def greet(self):
    print("にゃん（甘え）")


# Main
# ContextPy implimented by OOP
if __name__ == '__main__':
    print('Greeting implimented by CROSPy')

    p = Person("優太")
    c = Cat("にゃんた")

    p.greet()
    c.greet()
    p.activate('jp')
    p.greet()
    c.greet()
    p.apologize()
    c.fawn_on()
    c.deactivate('jp')
    p.apologize()
    c.fawn_on()

    # person base greet
    # cat base greet
    # こんにちは
    # にゃー
    # ごめんなさい
    # にゃん（甘え）
    # person base apologize
    # cat base fawn_on
