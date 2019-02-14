#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from my_context import *
import rospy

class T1BaseLayer(object):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1', dim4_1='dim4_1', dim1_2='dim1_2', dim2_2='dim2_2', dim4_2='dim4_2'):
        self.dim1_1 = dim1_1
        self.dim2_1 = dim2_1
        self.dim4_1 = dim4_1
        self.dim1_2 = dim1_2
        self.dim2_2 = dim2_2
        self.dim4_2 = dim4_2

    def context_method1(self):
        self.dim1_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim1_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim1_2

    def context_method2(self):
        self.dim2_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_1, self.dim2_2

    def context_method3(self):
        self.dim1_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim1_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim2_1, self.dim1_2, self.dim2_2

    def context_method4(self):
        self.dim1_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim1_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim4_1, self.dim1_2, self.dim4_2


class T1Layer1_1(T1BaseLayer):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1', dim4_1='dim4_1', dim1_2='dim1_2', dim2_2='dim2_2', dim4_2='dim4_2'):
        self.dim1_1 = dim1_1
        self.dim2_1 = dim2_1
        self.dim4_1 = dim4_1

    def context_method1(self):
        self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1

    def context_method2(self):
        self.dim2_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_1

    def context_method3(self):
        self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim2_1

    def context_method4(self):
        self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim4_1


class T1Layer1_2(T1BaseLayer):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1', dim4_1='dim4_1', dim1_2='dim1_2', dim2_2='dim2_2', dim4_2='dim4_2'):
        self.dim1_1 = dim1_1
        self.dim2_1 = dim2_1
        self.dim4_1 = dim4_1

    def context_method1(self):
        self.dim1_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1

    def context_method2(self):
        self.dim2_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_1

    def context_method3(self):
        self.dim1_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim2_1

    def context_method4(self):
        self.dim1_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim4_1


class T1Layer2_1(T1BaseLayer):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1', dim4_1='dim4_1', dim1_2='dim1_2', dim2_2='dim2_2', dim4_2='dim4_2'):
        self.dim1_2 = dim1_2
        self.dim2_2 = dim2_2
        self.dim4_2 = dim4_2

    def context_method1(self):
        self.dim1_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_2

    def context_method2(self):
        self.dim2_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_2

    def context_method3(self):
        self.dim1_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_2, self.dim2_2

    def context_method4(self):
        self.dim1_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_2, self.dim4_2


class T1Layer2_2(T1BaseLayer):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1', dim4_1='dim4_1', dim1_2='dim1_2', dim2_2='dim2_2', dim4_2='dim4_2'):
        self.dim1_2 = dim1_2
        self.dim2_2 = dim2_2
        self.dim4_2 = dim4_2

    def context_method1(self):
        self.dim1_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_2

    def context_method2(self):
        self.dim2_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_2

    def context_method3(self):
        self.dim1_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_2, self.dim2_2

    def context_method4(self):
        self.dim1_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_2, self.dim4_2


class Test1(Context):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1', dim4_1='dim4_1', dim1_2='dim1_2', dim2_2='dim2_2', dim4_2='dim4_2'):
        super(Test1, self).__init__()
        self.dim1_1 = dim1_1
        self.dim2_1 = dim2_1
        self.dim4_1 = dim4_1
        self.dim1_2 = dim1_2
        self.dim2_2 = dim2_2
        self.dim4_2 = dim4_2

    def context_method1(self):
        for l in reversed(self.layers):
            self.change(l)
            self.test1.context_method1()

    def context_method2(self):
        for l in reversed(self.layers):
            self.change(l)
            self.test1.context_method2()

    def context_method3(self):
        for l in reversed(self.layers):
            self.change(l)
            self.test1.context_method3()

    def context_method4(self):
        for l in reversed(self.layers):
            self.change(l)
            self.test1.context_method4()

    def change(self, layer):
        if 'base' == layer:
            self.test1 = T1BaseLayer(self.dim1_1, self.dim2_1, self.dim4_1, self.dim1_2, self.dim2_2, self.dim4_2)
        elif 'layer1_1' == layer:
            self.test1 = T1Layer1_1(self.dim1_1, self.dim2_1, self.dim4_1, self.dim1_2, self.dim2_2, self.dim4_2)
        elif 'layer1_2' == layer:
            self.test1 = T1Layer1_2(self.dim1_1, self.dim2_1, self.dim4_1, self.dim1_2, self.dim2_2, self.dim4_2)
        elif 'layer2_1' == layer:
            self.test1 = T1Layer2_1(self.dim1_2, self.dim2_2, self.dim4_2, self.dim1_2, self.dim2_2, self.dim4_2)
        elif 'layer2_2' == layer:
            self.test1 = T1Layer2_2(self.dim1_2, self.dim2_2, self.dim4_2, self.dim1_2, self.dim2_2, self.dim4_2)


# Main
if __name__ == '__main__':
    print('Sample implimented by OOP')

    rospy.init_node('simple_oop', anonymous=True)
    t1 = Test1()
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        t1.context_method1()
        rate.sleep()

    # t1 = Test1()
    # t1.context_method1_1()
    # t1.context_method2_1()
    # print ("------------------------")
    # t1.activate('layer1_1')
    # t1.context_method1_1()
    # t1.context_method2_1()
