#coding=utf-8
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

class MercedesFactory(object):
    """梅赛德斯工厂
    """
    def product_car(self):
        return Mercedes()

class BMWFactory(object):
    """宝马工厂
    """
    def product_car(self):
        return BMW()


if __name__ == '__main__':
    c1 = MercedesFactory().product_car()
    c2 = BMWFactory().product_car()
    print(c1)
    print(c2)
