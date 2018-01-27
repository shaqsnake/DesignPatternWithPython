#coding=utf-8
class Singleton(object):
    """单例类
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    """实际生成实例的类
    """
    def __init__(self, arg):
        self.foo = arg

    def display(self):
        return (id(self), self.foo)


if __name__ == "__main__":
    s1 = MyClass("bar")
    s2 = MyClass("zoo")
    print(s1.display())
    print(s2.display())
    assert s1 is s2
