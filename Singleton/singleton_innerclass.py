#coding=utf-8
class Singleton:
    """单列类
    """
    class __MyClass:
        """实际生成实例的类
        """
        def __init__(self, arg):
            """初始化并赋值"""
            self.foo = arg

        def display(self):
            """返回实例的id和属性值"""
            return (id(self), self.foo)

    # 类属性
    _instance = None
    def __init__(self, arg):
        if not Singleton._instance:
            Singleton._instance = Singleton.__MyClass(arg)
        else:
            Singleton._instance.foo = arg

    def __getattr__(self, attr):
        return getattr(self._instance, attr)


if __name__ == "__main__":
    """测试"""
    s1 = Singleton("bar")
    s2 = Singleton("zoo")
    print(s1.display())
    print(s2.display())
