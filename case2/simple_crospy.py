#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from crospy import *

class Test1(CROS):
    def __init__(self, dim1_1='dim1_1', dim2_1='dim2_1', dim4_1='dim4_1', dim1_2='dim1_2', dim2_2='dim2_2', dim4_2='dim4_2'):
        super(Test1, self).__init__()
        self.dim1_1 = dim1_1
        self.dim2_1 = dim2_1
        self.dim4_1 = dim4_1
        self.dim1_2 = dim1_2
        self.dim2_2 = dim2_2
        self.dim4_2 = dim4_2

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

    @cpybase
    def context_method3(self):
        self.dim1_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim1_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim2_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim2_1, self.dim1_2, self.dim2_2

    @cpybase
    def context_method4(self):
        self.dim1_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_1 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim1_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        self.dim4_2 = "base : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
        print self.dim1_1, self.dim4_1, self.dim1_2, self.dim4_2

@cpylayer(Test1, 'layer1_1', 'context_method1')
def context_method1(self):
    self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_1
    self.proceed()

@cpylayer(Test1, 'layer1_1', 'context_method2')
def context_method2(self):
    self.dim2_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim2_1
    self.proceed()

@cpylayer(Test1, 'layer1_1', 'context_method3')
def context_method3(self):
    self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    self.dim2_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_1, self.dim2_1
    self.proceed()

@cpylayer(Test1, 'layer1_1', 'context_method4')
def context_method4(self):
    self.dim1_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    self.dim4_1 = "layer1_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_1, self.dim4_1
    self.proceed()


@cpylayer(Test1, 'layer1_2', 'context_method1')
def context_method1(self):
    self.dim1_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_1
    self.proceed()

@cpylayer(Test1, 'layer1_2', 'context_method2')
def context_method2(self):
    self.dim2_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim2_1
    self.proceed()

@cpylayer(Test1, 'layer1_2', 'context_method3')
def context_method3(self):
    self.dim1_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    self.dim2_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_1, self.dim2_1
    self.proceed()

@cpylayer(Test1, 'layer1_2', 'context_method4')
def context_method4(self):
    self.dim1_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    self.dim4_1 = "layer1_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_1, self.dim4_1
    self.proceed()


@cpylayer(Test1, 'layer2_1', 'context_method1')
def context_method1(self):
    self.dim1_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_2
    self.proceed()

@cpylayer(Test1, 'layer2_1', 'context_method2')
def context_method2(self):
    self.dim2_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim2_2
    self.proceed()

@cpylayer(Test1, 'layer2_1', 'context_method3')
def context_method3(self):
    self.dim1_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    self.dim2_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_2, self.dim2_2
    self.proceed()

@cpylayer(Test1, 'layer2_1', 'context_method4')
def context_method4(self):
    self.dim1_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    self.dim4_2 = "layer2_1 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_2, self.dim4_2
    self.proceed()


@cpylayer(Test1, 'layer2_2', 'context_method1')
def context_method1(self):
    self.dim1_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_2
    self.proceed()

@cpylayer(Test1, 'layer2_2', 'context_method2')
def context_method2(self):
    self.dim2_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim2_2
    self.proceed()

@cpylayer(Test1, 'layer2_2', 'context_method3')
def context_method3(self):
    self.dim1_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    self.dim2_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_2, self.dim2_2
    self.proceed()

@cpylayer(Test1, 'layer2_2', 'context_method4')
def context_method4(self):
    self.dim1_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    self.dim4_2 = "layer2_2 : " + self.__class__.__name__ + " : " + sys._getframe().f_code.co_name
    print self.dim1_2, self.dim4_2
    self.proceed()


# Main
if __name__ == '__main__':
    print('Sample implimented by CROSPy')

    count = 0

    rospy.init_node('simple_crospy', anonymous=True)
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
    # t1.context_method1_1()
    # t1.context_method2_1()
    # print ("------------------------")
    # t1.activate('layer1_1')
    # t1.context_method1_1()
    # t1.context_method2_1()
