#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from my_context import *

class T1BaseLayer(object):
    def __init__(self, dim1='dim1', dim2="dim2"):
        self.dim1 = dim1
        self.dim2 = dim2

    def context_method1(self):
        self.dim1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1, self.dim2


class T1Layer1_1(T1BaseLayer):
    def __init__(self, dim1='dim1', dim2="dim2"):
        self.dim1 = dim1

    def context_method1(self):
        self.dim1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1

class T1Layer1_2(T1BaseLayer):
    def __init__(self, dim1='dim1', dim2="dim2"):
        self.dim1 = dim1

    def context_method1(self):
        self.dim1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1

class T1Layer2_1(T1BaseLayer):
    def __init__(self, dim1='dim1', dim2="dim2"):
        self.dim2 = dim2

    def context_method1(self):
        self.dim2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2

class T1Layer2_2(T1BaseLayer):
    def __init__(self, dim1='dim1', dim2="dim2"):
        self.dim2 = dim2

    def context_method1(self):
        self.dim2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2

class Test1(Context):
    def __init__(self, dim1='dim1', dim2='dim2'):
        super(Test1, self).__init__()
        self.dim1 = dim1
        self.dim2 = dim2

    def context_method1(self):
        for l in reversed(self.layers):
            self.change(l)
            self.test1.context_method1()

    def change(self, layer):
        if 'base' == layer:
            self.test1 = T1BaseLayer(self.dim1, self.dim2)
        elif 'layer1_1' == layer:
            self.test1 = T1Layer1_1(self.dim1, self.dim2)
        elif 'layer1_2' == layer:
            self.test1 = T1Layer1_2(self.dim1, self.dim2)
        elif 'layer2_1' == layer:
            self.test1 = T1Layer2_1(self.dim1, self.dim2)
        elif 'layer2_2' == layer:
            self.test1 = T1Layer2_2(self.dim1, self.dim2)
        else:
            pass


# Main
if __name__ == '__main__':
    print('Sample implimented by OOP')

    t1 = Test1()
    t1.context_method1()
    print ("------------------------")
    t1.activate('layer1_1')
    t1.context_method1()
    print ("------------------------")
    t1.activate('layer2_1')
    t1.context_method1()
