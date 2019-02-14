#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from my_context import *
import rospy

class Test1(Context):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1', dim4_1='dim4_1', dim1_2='dim1_2', dim2_2='dim2_2', dim4_2='dim4_2'):
        super(Test1, self).__init__()
        self.dim1_1 = dim1_1
        self.dim2_1 = dim2_1
        self.dim4_1 = dim4_1
        self.dim1_2 = dim1_2
        self.dim2_2 = dim2_2
        self.dim4_2 = dim4_2

    def change(self, layer):
        if 'base' == layer:
            self.m1 = self.context_method1_base
            self.m2 = self.context_method2_base
            self.m3 = self.context_method3_base
            self.m4 = self.context_method4_base
        elif 'layer1_1' == layer:
            self.m1 = self.context_method1_layer1_1
            self.m2 = self.context_method2_layer1_1
            self.m3 = self.context_method3_layer1_1
            self.m4 = self.context_method4_layer1_1
        elif 'layer1_2' == layer:
            self.m1 = self.context_method1_layer1_2
            self.m2 = self.context_method2_layer1_2
            self.m3 = self.context_method3_layer1_2
            self.m4 = self.context_method4_layer1_2
        elif 'layer2_1' == layer:
            self.m1 = self.context_method1_layer2_1
            self.m2 = self.context_method2_layer2_2
            self.m3 = self.context_method3_layer2_2
            self.m4 = self.context_method4_layer2_2

    def context_method1(self):
        for l in reversed(self.layers):
            self.change(l)
            self.m1()

    def context_method2(self):
        for l in reversed(self.layers):
            self.change(l)
            self.m2()

    def context_method3(self):
        for l in reversed(self.layers):
            self.change(l)
            self.m3()

    def context_method4(self):
        for l in reversed(self.layers):
            self.change(l)
            self.m4()

    def context_method1_base(self):
        self.dim1_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim1_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim1_2

    def context_method1_layer1_1(self):
        self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1

    def context_method1_layer1_2(self):
        self.dim1_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1

    def context_method1_layer2_1(self):
        self.dim1_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_2

    def context_method2_base(self):
        self.dim2_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_1, self.dim2_2

    def context_method2_layer1_1(self):
        self.dim2_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_1

    def context_method2_layer1_2(self):
        self.dim2_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_1

    def context_method2_layer2_1(self):
        self.dim2_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim2_2

    def context_method3_base(self):
        self.dim1_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim1_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim2_1, self.dim1_2, self.dim2_2

    def context_method3_layer1_1(self):
        self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim2_1

    def context_method3_layer1_2(self):
        self.dim1_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim2_1

    def context_method3_layer2_1(self):
        self.dim1_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_2, self.dim2_2

    def context_method4_base(self):
        self.dim1_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim1_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim4_1, self.dim1_2, self.dim4_2

    def context_method4_layer1_1(self):
        self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim4_1

    def context_method4_layer1_2(self):
        self.dim1_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim4_1

    def context_method4_layer2_1(self):
        self.dim1_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_2, self.dim4_2


# Main
if __name__ == '__main__':
    print('Sample primitive implimented')
    rospy.init_node('simple_primitive', anonymous=True)

    count = 0

    #rospy.init_node('simple_oop', anonymous=True)
    t1 = Test1()
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        t1.context_method1()
        if count%2 == 0:
            t1.activate('layer1_1')
        else:
            t1.deactivate('layer1_1')
        count+=1
        rate.sleep()

    # t1 = Test1()
    # t1.context_method1()
    # t1.context_method2()
    # print ("------------------------")
    # t1.activate('layer1_1')
    # t1.context_method1()
    # t1.context_method2()
