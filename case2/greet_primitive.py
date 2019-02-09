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
            elif 'name' == c:
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
            elif 'name' == c:
                pass
            else:
                pass

    def speak(self):
        for c in reversed(self.layers):
            if 'base' == c:
                self.greet()
                break
            elif 'jp' == c:
                pass
            elif 'name' == c:
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
