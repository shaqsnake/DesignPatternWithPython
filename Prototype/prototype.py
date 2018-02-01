#coding=utf-8
class Foo(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "id: {}, x: {}, y: {}".format(id(self), self.x, self.y)

if __name__ == '__main__':
    foo = Foo(1, 2)
    # 利用deepcopy获得新对象
    import copy
    foo1 = copy.deepcopy(foo)
    foo1.x = 3
    foo1.y = 4
    print(foo, foo1)

    # 利用__class__方法获得新对象
    foo2 = foo1.__class__(5, 6)
    print(foo, foo2)
