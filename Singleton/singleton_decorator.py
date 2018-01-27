#coding=utf-8
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class MyClass:
    """实际生成实例的类
    """
    foo = "foo"
    def display(self):
        return (id(self))

@singleton
class OtherClass:
    """另一个类
    """
    pass

if __name__ == "__main__":
    s1 = MyClass()
    s1.foo = "bar"
    print(s1.display(), s1.foo)
    s2 = MyClass()
    s2.foo = "zoo"
    print(s2.display(), s2.foo)
    assert s1 is s2
    s3 = OtherClass()
    s4 = OtherClass()
    assert s3 is s4
