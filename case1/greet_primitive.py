#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Context(object):
    def __init__(self, context=['base']):
        self.context = context

    def activate(self, layer):
        if not layer == 'base':
            self.context.append(layer)

    def deactivate(self, layer):
        if not layer == 'base':
            self.context.remove(layer)

    def change(self):
        pass

class Person(Context):
    def __init__(self, name='', context=['base']):
        super(Person, self).__init__(context)
        self.name = name

    def speak(self):
        self.greet()

    def greet(self):
        for c in reversed(self.context):
            if 'base' == c:
                self.greet_base()
                break
            elif 'jp' == c:
                self.greet_jp()
                break
            else:
                pass

    def my_name(self):
        pass

    def greet_base(self):
        print("base greet")

    def greet_jp(self):
        print("こんにちは")

# Main
if __name__ == '__main__':
    print('Sample primitive implimented')

    a = Person('優太')

    a.speak()
    a.activate('jp')
    a.speak()

    # result
    # base greet
    # こんにちは
