#coding=utf-8
import abc


class Mercedes(object):
    """梅赛德斯
    """
    def __repr__(self):
        return "Mercedes-Benz"

class BMW(object):
    """宝马
    """
    def __repr__(self):
        return "BMW"

class AbstractFactory(object):
    """抽象工厂
    """
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def product_car(self):
        pass

class MecedesFactory(AbstractFactory):
    """梅赛德斯工厂
    """
    def product_car(self):
        return Mercedes()

class BMWFactory(AbstractFactory):
    """宝马工厂
    """
    def product_car(self):
        return BMW()

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
    print(c1)
    f2 = Factory.get_factory('bf')
    c2 = f2.product_car()
    print(c2)
