class Singleton(object):
    """
    """
    class _A(object):
        def __init__(self):
            pass
                
        def display(self):
            """
            :return 
            """
            return id(self)

    _instance = None
    
    def __init__(self):
        """
        """
        if Singleton._instance is None:
            Singleton._instance = Singleton._A()

    def __getattr__(self, attr):
        return getattr(self._instance, attr)

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1), s1.display())
    print(id(s2), s2.display())

