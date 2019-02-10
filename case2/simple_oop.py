#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from my_context import *

class T1BaseLayer(object):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1'):
        self.dim1_1 = dim1_1
        self.dim2_1 = dim2_1

    def context_method1_1(self):
        self.dim1_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1

    def context_method2_1(self):
        self.dim2_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_1


class T1Layer1_1(T1BaseLayer):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1'):
        self.dim1_1 = dim1_1
        self.dim2_1 = dim2_1

    def context_method1_1(self):
        self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1

    def context_method2_1(self):
        self.dim2_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_1


class Test1(Context):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1'):
        super(Test1, self).__init__()
        self.dim1_1 = dim1_1
        self.dim2_1 = dim2_1

    def context_method1_1(self):
        for l in reversed(self.layers):
            self.change(l)
            self.test1.context_method1_1()

    def context_method2_1(self):
        for l in reversed(self.layers):
            self.change(l)
            self.test1.context_method2_1()

    def change(self, layer):
        if 'base' == layer:
            self.test1 = T1BaseLayer(self.dim1_1, self.dim2_1)
        elif 'layer1_1' == layer:
            self.test1 = T1Layer1_1(self.dim1_1, self.dim2_1)
        else:
            pass


# Main
if __name__ == '__main__':
    print('Sample implimented by OOP')

    t1 = Test1()
    t1.context_method1_1()
    t1.context_method2_1()
    print ("------------------------")
    t1.activate('layer1_1')
    t1.context_method1_1()
    t1.context_method2_1()
