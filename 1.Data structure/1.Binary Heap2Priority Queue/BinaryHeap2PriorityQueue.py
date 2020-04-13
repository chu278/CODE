class MaxPriorityQueue():
    def __init__(self, cap):
        self.mpq = []
        self.N = 0

    @staticmethod
    def parent(root: int):
        return root / 2

    @staticmethod
    def left(root: int):
        return root * 2

    @staticmethod
    def right(root: int):
        return root * 2 + 1

    def max(self):
        if len(self.mpq) > 1:
            return self.mpq[1]

    def insert(self, element):
        pass

    def del_max(self):
        pass

    def swim(self, k: int):
        pass

    def sink(self, k: int):
        pass

    def exchange(self, a: int, b: int):
        pass

    def less(self, a: int, b: int):
        return self.mpq[a] < self.mpq[b]
