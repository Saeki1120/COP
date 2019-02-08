#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from crospy import *

class Test1(CPy):
    def __init__(self):
        super(Test1, self).__init__()
        self.arg1 = "arg1"
        self.arg2 = "arg2"
        self.arg3 = "arg3"

    def method1(self):
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    @cpybase
    def context_method1(self):
        print "base"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

class Test2(CPy):
    def __init__(self):
        super(Test2, self).__init__()
        self.arg1 = "arg1"
        self.arg2 = "arg2"
        self.arg3 = "arg3"

    def method1(self):
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

    @cpybase
    def context_method1(self):
        print "base"
        print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

@cpylayer(Test1, 'layer1_1', 'context_method1')
def context_method1(self):
    print "layer1_1"
    print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

@cpylayer(Test1, 'layer1_2', 'context_method1')
def context_method1(self):
    print "layer1_2"
    print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

@cpylayer(Test2, 'layer1_1', 'context_method1')
def context_method1(self):
    print "layer1_1"
    print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

@cpylayer(Test2, 'layer1_2', 'context_method1')
def context_method1(self):
    print "layer1_2"
    print self.__class__.__name__ + " : " + sys._getframe().f_code.co_name

# Main
# ContextPy implimented by OOP
if __name__ == '__main__':
    print('Sample implimented by CROSPy')

    t1 = Test1()
    t2 = Test2()
    t1.context_method1()
    t2.context_method1()
    print ("------------------------")
    t1.activate('layer1_1')
    t1.context_method1()
    t2.context_method1()
    print ("------------------------")
    t1.activate('layer1_2')
    t1.context_method1()
    t2.context_method1()
