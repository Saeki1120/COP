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

class T1BaseLayer(object):
    def context_method1(self):
        print "base"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

class T1Layer1_1(T1BaseLayer):
    def context_method1(self):
        print "layer1_1"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

class T1Layer1_2(T1BaseLayer):
    def context_method1(self):
        print "layer1_2"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

class T2BaseLayer(object):
    def context_method1(self):
        print "base"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

class T2Layer1_1(T2BaseLayer):
    def context_method1(self):
        print "layer1_1"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

class T2Layer1_2(T2BaseLayer):
    def context_method1(self):
        print "layer1_2"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

# Context Object 1
class Test1(Context):
    def __init__(self, arg=''):
        super(Test1, self).__init__()
        self.arg1 = "arg1"
        self.arg2 = "arg2"
        self.arg3 = "arg3"
        self._layer = T1BaseLayer()

    def method1(self):
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    def context_method1(self):
        self.change()
        self._layer.context_method1()

    def change(self):
        for l in reversed(self.layers):
            if 'base' == l:
                self._layer = T1BaseLayer()
                break
            elif 'layer1_1' == l:
                self._layer = T1Layer1_1()
                break
            elif 'layer1_2' == l:
                self._layer = T1Layer1_2()
                break
            else:
                pass

# Context Object 2
class Test2(Context):
    def __init__(self):
        super(Test2, self).__init__()
        self.arg1 = "arg1"
        self.arg2 = "arg2"
        self.arg3 = "arg3"
        self._layer = T2BaseLayer()

    def method1(self):
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    def context_method1(self):
        self.change()
        self._layer.context_method1()

    def change(self):
        for l in reversed(self.layers):
            if 'base' == l:
                self._layer = T2BaseLayer()
                break
            elif 'layer1_1' == l:
                self._layer = T2Layer1_1()
                break
            elif 'layer1_2' == l:
                self._layer = T2Layer1_2()
                break
            else:
                pass


# Main
if __name__ == '__main__':
    print('Sample implimented by OOP')

    t1 = Test1()
    t2 = Test2()
    t1.context_method1()
    t2.context_method1()
    t1.activate('layer1_1')
    t1.context_method1()
    t2.context_method1()
    t2.activate('layer1_2')
    t1.context_method1()
    t2.context_method1()
