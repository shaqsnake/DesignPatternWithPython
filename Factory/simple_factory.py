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

class SimpleCarFactory(object):
    """简单工厂
    """
    @staticmethod
    def product_car(name):
        if name == 'mb':
            return Mercedes()
        elif name == 'bmw':
            return BMW()


if __name__ == '__main__':
    c1 = SimpleCarFactory.product_car('mb')
    c2 = SimpleCarFactory.product_car('bmw')
    print(c1, c2)
