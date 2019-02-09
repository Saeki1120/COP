#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_context import *

class PLanguage(object):
    def greet(self):
        print("person base greet")

class PJapanese(PLanguage):
    def greet(self):
        print("こんにちは")

class CLanguage(object):
    def greet(self):
        print("cat base greet")

class CJapanese(CLanguage):
    def greet(self):
        print("にゃー")

class Person(Context):
    def __init__(self, name=''):
        super(Person, self).__init__()
        self.name = name
        self.lang = self.change()

    def my_name(self):
        print(self.name)

    def greet(self):
        self.change()
        self.lang.greet()

    def change(self):
        for c in reversed(self.layers):
            if 'base' == c:
                self.lang = PLanguage()
                break
            elif 'jp' == c:
                self.lang = PJapanese()
                break
            else:
                pass


class Cat(Context):
    def __init__(self, name=''):
        super(Cat, self).__init__()
        self.name = name
        self.lang = self.change()

    def my_name(self):
        print(self.name)

    def greet(self):
        self.change()
        self.lang.greet()

    def change(self):
        for c in reversed(self.layers):
            if 'base' == c:
                self.lang = CLanguage()
                break
            elif 'jp' == c:
                self.lang = CJapanese()
                break
            else:
                pass


# Main
# ContextPy implimented by OOP
if __name__ == '__main__':
    print('Greeting implimented by OOP')

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
    # Activated
    # ['base', 'jp']
    # こんにちは
    # にゃー
    # Deactivated
    # ['base']
    # person base greet
    # cat base greet
