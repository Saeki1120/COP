#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crospy import *

class Person(CPy):
    def __init__(self, name=''):
        super(Person, self).__init__()
        self.name = name

    def speak(self):
        self.greet()

    @cpybase
    def greet(self):
        print("base greet")

    def my_name(self):
        pass

@cpylayer(Person, 'jp', 'greet')
def greet(self):
    print("こんにちは")


# Main
# ContextPy implimented by OOP
if __name__ == '__main__':
    print('Sample implimented by CROSPy')

    a = Person("優太")

    a.speak()
    a.activate('jp')
    a.speak()
