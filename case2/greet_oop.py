#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_context import *

class PLanguage(object):
    def __init__(self, name=''):
        self.name = name

    def my_name(self):
        print(self.name)

    def greet(self):
        print("person base greet")

class PJapanese(PLanguage):
    def __init__(self, name=''):
        super(PJapanese, self).__init__(name)

    def greet(self):
        print("こんにちは")

class PLName(PLanguage):
    def __init__(self, name=''):
        super(PLName, self).__init__(name)

    def greet(self):
        self.my_name()
        super(PLName, self).greet()

class PJName(PJapanese):
    def __init__(self, name=''):
        super(PJName, self).__init__(name)

    def greet(self):
        self.my_name()
        super(PJName, self).greet()

class CLanguage(object):
    def __init__(self, name=''):
        self.name = name

    def my_name(self):
        print(self.name)

    def greet(self):
        print("cat base greet")

class CJapanese(CLanguage):
    def __init__(self, name=''):
        super(CJapanese, self).__init__(name)

    def greet(self):
        print("にゃー")

class CName(CLanguage):
    def __init__(self, name=''):
        super(CName, self).__init__(name)

    def greet(self):
        self.my_name()
        super(CName, self).greet()

class CJapaneseName(CLanguage):
    def __init__(self, name=''):
        super(CJapaneseName, self).__init__(name)

    def greet(self):
        self.my_name()
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
        name_flag = False
        for c in reversed(self.layers):
            if 'base' == c:
                if not name_flag:
                    self.lang = PLanguage(self.name)
                    break
                else:
                    break
            elif 'jp' == c:
                if not name_flag:
                    self.lang = PJapanese(self.name)
                    break
                else:
                    self.lang = PJName(self.name)
                    break
            elif 'name' == c:
                self.lang = PLName(self.name)
                name_flag = True
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
        name_flag = False
        jp_flag = False
        for c in reversed(self.layers):
            if 'base' == c:
                if not (name_flag or jp_flag) :
                    self.lang = CLanguage(self.name)
                    break
                else:
                    break
            elif 'jp' == c:
                if not name_flag:
                    self.lang = CJapanese(self.name)
                    jp_flag = True
                else:
                    self.lang = CJapaneseName(self.name)
                    break
            elif 'name' == c:
                if not jp_flag:
                    self.lang = CName(self.name)
                    name_flag = True
                else:
                    self.lang = CJapaneseName(self.name)
                    name_flag = True
                    break
            else:
                pass

        # for c in reversed(self.layers):
        #     if 'base' == c:
        #         self.lang = CLanguage(self.name)
        #         break
        #     elif 'jp' == c:
        #         self.lang = CJapanese(self.name)
        #         break
        #     elif 'name' == c:
        #         self.lang = CName(self.name)
        #         break
        #     else:
        #         pass


# Main
# ContextPy implimented by OOP
if __name__ == '__main__':
    print('Greeting implimented by OOP')

    p = Person("優太")
    c = Cat("にゃんた")

    p.greet()
    c.greet()
    print ("------------")
    p.activate('jp')
    p.greet()
    c.greet()
    print ("------------")
    c.activate('name')
    p.greet()
    c.greet()
    print ("------------")
    c.deactivate('jp')
    c.activate('jp')
    p.greet()
    c.greet()
    print ("------------")
    p.deactivate('jp')
    p.greet()
    c.greet()

    # person base greet
    # cat base greet
    # ------------
    # Activated
    # ['base', 'jp']
    # こんにちは
    # にゃー
    # ------------
    # Activated
    # ['base', 'jp', 'name']
    # 優太
    # こんにちは
    # にゃんた
    # にゃー
    # ------------
    # Deactivated
    # ['base', 'name']
    # Activated
    # ['base', 'name', 'jp']
    # こんにちは
    # にゃんた
    # にゃー
    # ------------
    # Deactivated
    # ['base', 'name']
    # 優太
    # person base greet
    # にゃんた
    # cat base greet
