#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_context import *

class PLanguage(object):
    def greet(self):
        print("person base greet")

    def apologize(self):
        print("person base apologize")

class PJapanese(PLanguage):
    def greet(self):
        print("こんにちは")

    def apologize(self):
        print("ごめんなさい")

class CLanguage(object):
    def greet(self):
        print("cat base greet")

    def fawn_on(self):
        print("cat base fawn_on")

class CJapanese(CLanguage):
    def greet(self):
        print("にゃー")

    def fawn_on(self):
        print("にゃん（甘え）")

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

    def apologize(self):
        self.change()
        self.lang.apologize()

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

    def fawn_on(self):
        self.change()
        self.lang.fawn_on()

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
    p.apologize()
    c.fawn_on()
    c.deactivate('jp')
    p.apologize()
    c.fawn_on()

    # person base greet
    # cat base greet
    # Activated
    # ['base', 'jp']
    # こんにちは
    # にゃー
    # ごめんなさい
    # にゃん（甘え）
    # Deactivated
    # ['base']
    # person base apologize
    # cat base fawn_on
