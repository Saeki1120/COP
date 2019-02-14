#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

class Context(object):
    layers = ['base']

    def __init__(cls):
        cls.init_layer()
        cls.async_init()

    @classmethod
    def init_layer(cls):
        if not hasattr(cls, 'layers'):
            cls.layers = ['base']

    @classmethod
    def activate_local(cls, layer):
        if not layer == 'base':
            cls.layers.append(layer)
            print("Activated")
            print(cls.layers)

    @classmethod
    def deactivate_local(cls, layer):
        if not layer == 'base':
            if layer in cls.layers:
                cls.layers.remove(layer)
                print("Deactivated")
                print(cls.layers)

    def change(self):
        pass

    def async_init(self):
        def handle_activate(data):
            if rospy.get_name() != data._connection_header['callerid']:
                Context.activate_local(data.data)

        def handle_deactivate(data):
            if rospy.get_name() != data._connection_header['callerid']:
                Context.deactivate_local(data.data)

        # for activate
        topic = 'cros' + '/activate'
        self.actpub = rospy.Publisher(topic, String, queue_size=10)
        self.actsub = rospy.Subscriber(topic, String, handle_activate)
        # for deactivate
        topic = 'cros' + '/deactivate'
        self.deactpub = rospy.Publisher(topic, String, queue_size=10)
        self.deactsub = rospy.Subscriber(topic, String, handle_deactivate)

    def send_activate(self, layer):
            self.actpub.publish(layer)

    def send_deactivate(self, layer):
            self.deactpub.publish(layer)

    # user can call this activation method
    def activate(self, layer):
        self.send_activate(layer)
        Context.activate_local(layer)

    # user can call this dectivation method
    def deactivate(self, layer):
        self.send_deactivate(layer)
        Context.deactivate_local(layer)
