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

    @classmethod
    def deactivate(cls, layer):
        if not layer == 'base':
            cls.layers.remove(layer)

    def change(self):
        pass

class Person(Context):
    def __init__(self, name=''):
        super(Person, self).__init__()
        self.name = name

    def speak(self):
        self.greet()

    def greet(self):
        for c in reversed(self.layers):
            if 'base' == c:
                self.greet_base()
                break
            elif 'jp' == c:
                self.greet_jp()
                break
            else:
                pass

    def my_name(self):
        print(self.name)

    def buy_house(self, price, address):
        self.house = House(price, address)

    def my_house(self):
        if hasattr(self, 'house'):
            self.house.get_address()
            self.house.get_price()
        else:
            print("can't show because you don't have a house")

    def buy_cat(self, price, cat):
        if hasattr(self, 'cat'):
            print("you have already buy a cat")
        else:
            if price >= cat.value:
                self.cat = cat
            else:
                print("can't buy because you don't have enough money")

    def play_cat(self):
        if hasattr(self, 'cat'):
            self.cat.play_cat()
        else:
            print("can't play because you don't have a cat")

    def greet_base(self):
        print("base greet")

    def greet_jp(self):
        print("こんにちは")

class House(Context):
    def __init__(self, price=0, address=''):
        super(House, self).__init__()
        self.set_price(price)
        self.address = address

    def get_address(self):
        print(self.address)

    def set_price(self, price):
        self.price = (self.layers[-1], price)

    def get_price(self):
        for c in reversed(self.layers):
            if 'base' == c:
                self.get_price_base()
                break
            elif 'jp' == c:
                self.get_price_jp()
                break
            else:
                pass

    def get_price_base(self):
        print(self.price)

    def get_price_jp(self):
        if 'base' == self.price[0]:
            print(str(self.price[1]))
        elif 'jp' == self.price[0]:
            print(str(self.price[1]) + "円")
        else:
            pass

class Cat(Context):
    def __init__(self, name='', value=50):
        super(Cat, self).__init__()
        self.name = name
        self.value = value

    def play_cat(self):
        self.meow()

    def meow(self):
        for c in reversed(self.layers):
            if 'base' == c:
                self.meow_base()
                break
            elif 'jp' == c:
                self.meow_jp()
                break
            else:
                pass

    def my_name(self):
        pass

    def meow_base(self):
        print("base meow")

    def meow_jp(self):
        print("にゃー")


# Main
if __name__ == '__main__':
    print('Sample primitive implimented')

    a = Person('優太')
    c = Cat('ニャン太')

    a.speak()
    a.activate('jp')
    a.speak()
    a.my_house()
    a.buy_house(1000, '福岡')
    a.my_house()
    a.buy_cat(10, c)
    a.play_cat()
    a.buy_cat(100, c)
    a.play_cat()

    # result
    # base greet
    # こんにちは
