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


class Cat(CPy):
    def __init__(self, name=''):
        super(Cat, self).__init__()
        self.name = name

    def my_name(self):
        print(self.name)

    @cpybase
    def greet(self):
        print("cat base greet")

@cpylayer(Cat, 'jp', 'greet')
def greet(self):
    print("にゃー")


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
    c.deactivate('jp')
    p.greet()
    c.greet()

    # person base greet
    # cat base greet
    # こんにちは
    # にゃー
    # person base greet
    # cat base greet
