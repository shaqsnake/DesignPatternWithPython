class ReusablePool:
    """
    """
    def __init__(self, max_size):
        self._reusables = [Reusable() for _ in range(max_size)]

    def acquire(self):
        if len(_reusables):
            return self._reusables.pop()
        return TypeError("No reusable object!")

    def release(self, reusable):
        self._reusables.append(reusable)

class Reusable:
    pass


if __name__ == '__main__':
    reusable_pool = ReusablePool(3)
    reusable = reusable_pool.acquire()
    reusable_pool.release(reusable)
