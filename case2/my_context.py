#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
