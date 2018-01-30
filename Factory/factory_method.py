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

class MercedesFactory(AbstractFactory):
    """梅赛德斯工厂
    """
    def product_car(self):
        return Mercedes()

class BMWFactory(AbstractFactory):
    """宝马工厂
    """
    def product_car(self):
        return BMW()


if __name__ == '__main__':
    c1 = MercedesFactory().product_car()
    c2 = BMWFactory().product_car()
    print(c1)
    print(c2)
