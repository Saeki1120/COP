#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from my_context import *

class Test1(Context):
    def __init__(self, dim1="dim1", dim2="dim2"):
        super(Test1, self).__init__()
        self.dim1 = dim1
        self.dim2 = dim2

    def context_method1_1(self):
        for l in reversed(self.layers):
            if 'base' == l:
                self.context_method1_1_base()
            elif 'layer1_1' == l:
                self.context_method1_1_layer1_1()
            elif 'layer2_1' == l:
                self.context_method1_1_layer2_1()
            else:
                pass

    def context_method1_1_base(self):
        self.dim1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1, self.dim2

    def context_method1_1_layer1_1(self):
        self.dim1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1

    def context_method1_1_layer2_1(self):
        self.dim2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2


# Main
if __name__ == '__main__':
    print('Sample primitive implimented')

    t1 = Test1()
    t1.context_method1_1()
    print ("------------------------")
    t1.activate('layer1_1')
    t1.context_method1_1()
    print ("------------------------")
    t1.activate('layer2_1')
    t1.context_method1_1()
