#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_context import *

class PLanguage(object):
    def greet(self):
        print("person base greet")


class PJapanese(PLanguage):
    def greet(self):
        print("こんにちは")


class PEnglish(PLanguage):
    def greet(self):
        print("Hello")


class CLanguage(object):
    def greet(self):
        print("cat base greet")


class CJapanese(CLanguage):
    def greet(self):
        print("にゃー")


class CEnglish(CLanguage):
    def greet(self):
        print("mew")


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
        for l in reversed(self.layers):
            if 'base' == l:
                self.lang = PLanguage()
                break
            elif 'jp' == l:
                self.lang = PJapanese()
                break
            elif 'en' == l:
                self.lang = PEnglish()
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
        for l in reversed(self.layers):
            if 'base' == l:
                self.lang = CLanguage()
                break
            elif 'jp' == l:
                self.lang = CJapanese()
                break
            elif 'en' == l:
                self.lang = CEnglish()
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
    c.activate('en')
    p.greet()
    c.greet()

    # person base greet
    # cat base greet
    # Activated
    # ['base', 'jp']
    # こんにちは
    # にゃー
    # Activated
    # ['base', 'jp', 'en']
    # Hello
    # mew
