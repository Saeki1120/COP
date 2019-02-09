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
            elif 'name' == l:
                self.greet_name()
            else:
                pass

    def my_name(self):
        print(self.name)

    def greet_base(self):
        print("person base greet")

    def greet_jp(self):
        print("こんにちは")

    def greet_name(self):
        self.my_name()


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
            elif 'name' == l:
                pass
            else:
                pass

    def speak(self):
        for l in reversed(self.layers):
            if 'base' == l:
                self.greet()
                break
            elif 'jp' == l:
                pass
            elif 'name' == l:
                self.speak_name()
            else:
                pass

    def my_name(self):
        print(self.name)

    def greet_base(self):
        print("cat base greet")

    def greet_jp(self):
        print("にゃー")

    def speak_name(self):
        self.my_name()


# Main
if __name__ == '__main__':
    print('Greeting primitive implimented')

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

    # person base greet
    # cat base greet
    # ------------
    # Activated
    # ['base', 'jp']
    # こんにちは
    # cat base greet
    # ------------
    # Activated
    # ['base', 'jp', 'name']
    # 優太
    # こんにちは
    # にゃんた
    # cat base greet
    # ------------
    # Deactivated
    # ['base', 'name']
    # Activated
    # ['base', 'name', 'jp']
    # こんにちは
    # にゃんた
    # cat base greet
    # ------------
    # Deactivated
    # ['base', 'name']
    # 優太
    # person base greet
    # にゃんた
    # cat base greet
