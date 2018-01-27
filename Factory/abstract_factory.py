#coding=utf-8
import abc

# 两种小汽车
class Mercedes_C63(object):
    """梅赛德斯 C63
    """
    def __repr__(self):
        return "Mercedes-Benz: C63"

class BMW_M3(object):
    """宝马 M3
    """
    def __repr__(self):
        return "BMW: M3"

#　两种SUV
class Mercedes_G63(object):
    """梅赛德斯 G63
    """
    def __repr__(self):
        return "Mercedes-Benz: G63"

class BMW_X5(object):
    """宝马 X5
    """
    def __repr__(self):
        return "BMW: X5"

class AbstractFactory(object):
    """抽象工厂
    可以生产小汽车外，还可以生产SUV
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_car(self):
        pass

    @abc.abstractmethod
    def product_suv(self):
        pass

class MecedesFactory(AbstractFactory):
    """梅赛德斯工厂
    """
    def product_car(self):
        return Mercedes_C63()

    def product_suv(self):
        return Mercedes_G63()

class BMWFactory(AbstractFactory):
    """宝马工厂
    """
    def product_car(self):
        return BMW_M3()

    def product_suv(self):
        return BMW_X5()

class Factory(object):
    @staticmethod
    def get_factory(name):
        if name == 'mf':
            return MecedesFactory()
        elif name == 'bf':
            return BMWFactory()
        raise TypeError("Unkonwn Factory")

if __name__ == '__main__':
    f1 = Factory.get_factory('mf')
    c1 = f1.product_car()
    s1 = f1.product_suv()
    print(c1, s1)
    f2 = Factory.get_factory('bf')
    s2 = f2.product_suv()
    c2 = f2.product_car()
    print(c2, s2)
