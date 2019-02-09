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

@cpylayer(Person, 'jp', 'greet')
def greet(self):
    print("こんにちは")

@cpylayer(Person, 'name', 'greet')
def greet(self):
    self.my_name()
    self.proceed()


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
    def speak(self):
        self.greet()

@cpylayer(Cat, 'jp', 'greet')
def greet(self):
    print("にゃー")

@cpylayer(Cat, 'name', 'greet')
def greet(self):
    self.proceed()

@cpylayer(Cat, 'jp', 'speak')
def speak(self):
    self.proceed()

@cpylayer(Cat, 'name', 'speak')
def speak(self):
    self.my_name()
    self.proceed()


# Main
# ContextPy implimented by OOP
if __name__ == '__main__':
    print('Greeting implimented by CROSPy')

    p = Person("優太")
    c = Cat("にゃんた")

    p.greet()
    c.speak()
    print ("------------")
    p.activate('jp')
    p.greet()
    c.speak()
    print ("------------")
    c.activate('name')
    p.greet()
    c.speak()
    print ("------------")
    c.deactivate('jp')
    c.activate('jp')
    p.greet()
    c.speak()
    print ("------------")
    p.deactivate('jp')
    p.greet()
    c.speak()

    # Cat側は無理やり name jp と jp name で同じ振る舞いをさせ得るための実装

    # person base greet
    # cat base greet
    # ------------
    # こんにちは
    # にゃー
    # ------------
    # 優太
    # こんにちは
    # にゃんた
    # にゃー
    # ------------
    # こんにちは
    # にゃんた
    # にゃー
    # ------------
    # 優太
    # person base greet
    # にゃんた
    # cat base greet
