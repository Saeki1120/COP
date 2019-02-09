#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_context import *

class Person(Context):
    def __init__(self, name=''):
        super(Person, self).__init__()
        self.name = name

    def greet(self):
        for l in reversed(self.layers):
            if 'base' == l:
                self.greet_base()
                break
            elif 'jp' == l:
                self.greet_jp()
                break
            else:
                pass

    def apologize(self):
        for l in reversed(self.layers):
            if 'base' == l:
                self.apologize_base()
                break
            elif 'jp' == l:
                self.apologize_jp()
                break
            else:
                pass

    def my_name(self):
        print(self.name)

    def greet_base(self):
        print("person base greet")

    def greet_jp(self):
        print("こんにちは")

    def apologize_base(self):
        print("person base apologize")

    def apologize_jp(self):
        print("ごめんなさい")


class Cat(Context):
    def __init__(self, name=''):
        super(Cat, self).__init__()
        self.name = name

    def greet(self):
        for l in reversed(self.layers):
            if 'base' == l:
                self.greet_base()
                break
            elif 'jp' == l:
                self.greet_jp()
                break
            else:
                pass

    def fawn_on(self):
        for l in reversed(self.layers):
            if 'base' == l:
                self.fawn_on_base()
                break
            elif 'jp' == l:
                self.fawn_on_jp()
                break
            else:
                pass

    def my_name(self):
        print(self.name)

    def greet_base(self):
        print("cat base greet")

    def greet_jp(self):
        print("にゃー")

    def fawn_on_base(self):
        print("cat base fawn_on")

    def fawn_on_jp(self):
        print("にゃん（甘え）")


# Main
if __name__ == '__main__':
    print('Greeting primitive implimented')

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

    # result
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
