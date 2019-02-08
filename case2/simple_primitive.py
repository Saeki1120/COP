#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Context(object):
    layers = ['base']

    def __init__(cls):
        cls.init_layer()

    @classmethod
    def init_layer(cls):
        if not hasattr(cls, 'layers'):
            cls.layers = ['base']

    @classmethod
    def activate(cls, layer):
        if not layer == 'base':
            cls.layers.append(layer)
            print("Activated")
            print(cls.layers)

    @classmethod
    def deactivate(cls, layer):
        if not layer == 'base':
            cls.layers.remove(layer)
            print("Deactivated")
            print(cls.layers)

    def change(self):
        pass

# Context Object 1
class Test1(Context):
    def __init__(self, arg=''):
        super(Test1, self).__init__()
        self.arg1 = "arg1"
        self.arg2 = "arg2"
        self.arg3 = "arg3"


    def method1(self):
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    def context_method1(self):
        for l in reversed(self.layers):
            if 'base' == l:
                self.context_method1_base()
                break
            elif 'layer1_1' == l:
                self.context_method1_layer1_1()
                break
            elif 'layer1_2' == l:
                self.context_method1_layer1_2()
                break
            else:
                pass
    def context_method1_base(self):
        print "base"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    def context_method1_layer1_1(self):
        print "layer1_1"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    def context_method1_layer1_2(self):
        print "layer1_2"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

# Context Object 2
class Test2(Context):
    def __init__(self):
        super(Test2, self).__init__()
        self.arg1 = "arg1"
        self.arg2 = "arg2"
        self.arg3 = "arg3"

    def method1(self):
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    def context_method1(self):
        for l in reversed(self.layers):
            if 'base' == l:
                self.context_method1_base()
                break
            elif 'layer1_1' == l:
                self.context_method1_layer1_1()
                break
            elif 'layer1_2' == l:
                self.context_method1_layer1_2()
                break
            else:
                pass
    def context_method1_base(self):
        print "base"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    def context_method1_layer1_1(self):
        print "layer1_1"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    def context_method1_layer1_2(self):
        print "layer1_2"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

# Main
if __name__ == '__main__':
    print('Sample primitive implimented')

    t1 = Test1()
    t2 = Test2()
    t1.context_method1()
    t2.context_method1()
    t1.activate('layer1')
    t1.context_method1()
    t2.context_method1()
    t2.activate('layer1_2')
    t1.context_method1()
    t2.context_method1()
