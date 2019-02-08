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

class Language(object):
    def __init__(self):
        pass

    def greet(self):
        print("base greet")

class Japanese(Language):
    def __init__(self):
        super(Japanese, self).__init__()

    def greet(self):
        print("こんにちは")

class Person(Context):
    def __init__(self, name='', context=['base']):
        super(Person, self).__init__(context)
        self.name = name
        self.lang = self.change()

    def speak(self):
        self.greet()

    def greet(self):
        self.change()
        self.lang.greet()

    def my_name(self):
        pass

    def change(self):
        for c in reversed(self.context):
            if 'base' == c:
                self.lang = Language()
                break
            elif 'jp' == c:
                self.lang = Japanese()
                break
            else:
                pass

# Main
# ContextPy implimented by OOP
if __name__ == '__main__':
    print('Sample implimented by OOP')

    a = Person()
    time = 13

    a.speak()
    a.activate('jp')
    a.speak()
