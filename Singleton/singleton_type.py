#coding=utf-8
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        """重写，实现单例模式"""
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class MyClass(object):
    # 指定元类
    __metaclass__ = Singleton

    def display(self):
        return (id(self))


if __name__ == "__main__":
    s1 = MyClass()
    s2 = MyClass()
    print(s1.display())
    print(s2.display())
    assert s1 is s2
