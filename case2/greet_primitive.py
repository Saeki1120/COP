#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_context import *

class Person(Context):
    def __init__(self, name=''):
        super(Person, self).__init__()
        self.name = name

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

    def my_name(self):
        print(self.name)

    def greet_base(self):
        print("person base greet")

    def greet_jp(self):
        print("こんにちは")


class Cat(Context):
    def __init__(self, name='', value=50):
        super(Cat, self).__init__()
        self.name = name

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

    def my_name(self):
        print(self.name)

    def greet_base(self):
        print("cat base greet")

    def greet_jp(self):
        print("にゃー")


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
    c.deactivate('jp')
    p.greet()
    c.greet()

    # result
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
