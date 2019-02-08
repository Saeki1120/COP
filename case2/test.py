#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Context(object):
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

    @classmethod
    def deactivate(cls, layer):
        if not layer == 'base':
            cls.layers.remove(layer)

    def change(self):
        pass

if __name__ == '__main__':
    c1 = Context()
    c2 = Context()
    print c1.layers
    print c2.layers
    c1.activate('jp')
    print c1.layers
    print c2.layers
