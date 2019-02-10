#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from crospy import *

class Test1(CPy):
    def __init__(self, dim1_1='dim1_1', dim1_2='dim1_2', dim2_1='dim2_1', dim2_2='dim2_2'):
        super(Test1, self).__init__()
        self.dim1_1 = dim1_1
        self.dim1_2 = dim1_2
        self.dim2_1 = dim2_1
        self.dim2_2 = dim2_2

    @cpybase
    def context_method1(self):
        self.dim1_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim1_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim1_2

    @cpybase
    def context_method2(self):
        self.dim2_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_1, self.dim2_2

@cpylayer(Test1, 'layer1_1', 'context_method1')
def context_method1(self):
    self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_1
    self.proceed()

@cpylayer(Test1, 'layer1_2', 'context_method1')
def context_method1(self):
    self.dim1_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_1
    self.proceed()

@cpylayer(Test1, 'layer2_1', 'context_method1')
def context_method1(self):
    self.dim1_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_2
    self.proceed()

@cpylayer(Test1, 'layer2_2', 'context_method1')
def context_method1(self):
    self.dim1_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_2
    self.proceed()

@cpylayer(Test1, 'layer1_1', 'context_method2')
def context_method2(self):
    self.dim2_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim2_1
    self.proceed()

@cpylayer(Test1, 'layer1_2', 'context_method2')
def context_method2(self):
    self.dim2_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim2_1
    self.proceed()

@cpylayer(Test1, 'layer2_1', 'context_method2')
def context_method2(self):
    self.dim2_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim2_2
    self.proceed()

@cpylayer(Test1, 'layer2_2', 'context_method2')
def context_method2(self):
    self.dim2_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim2_2
    self.proceed()

# Main
if __name__ == '__main__':
    print('Sample implimented by CROSPy')

    t1 = Test1()
    t1.context_method1()
    t1.context_method2()
    print ("------------------------")
    t1.activate('layer1_1')
    t1.context_method1()
    t1.context_method2()
    print ("------------------------")
    t1.activate('layer1_2')
    t1.context_method1()
    t1.context_method2()
    print ("------------------------")
    t1.activate('layer2_1')
    t1.context_method1()
    t1.context_method2()
