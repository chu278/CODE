class MaxPriorityQueue():
    def __init__(self):
        self.mpq = [0]

    @staticmethod
    def parent(root: int):
        return int(root / 2)

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
        self.mpq.append(element)
        self.swim(len(self.mpq) - 1)

    def pop(self):
        self.exchange(1, len(self.mpq) - 1)
        top = self.mpq.pop()
        self.sink(1)
        return top

    def swim(self, k: int):
        while self.less(self.parent(k), k) and k > 1:
            self.exchange(k, self.parent(k))
            k = self.parent(k)

    def sink(self, k: int):
        while True:
            print(self.mpq)
            children = []
            if self.left(k) < len(self.mpq) and self.less(k, self.left(k)):
                children.append(self.left(k))
            if self.right(k) < len(self.mpq) and self.less(k, self.right(k)):
                children.append(self.right(k))
            print("k =", k)
            print("children =", children)
            if not children:
                break
            index = self.max_index(children)
            self.exchange(k, index)
            k = index

    def exchange(self, a: int, b: int):
        self.mpq[a], self.mpq[b] = self.mpq[b], self.mpq[a]

    def less(self, a: int, b: int) -> bool:
        return self.mpq[a] < self.mpq[b]

    def max_index(self, children):
        if len(children) == 1:
            return children[-1]
        else:
            if self.mpq[children[0]] > self.mpq[children[1]]:
                return children[0]
            else:
                return children[1]


max_pq = MaxPriorityQueue()
for i in range(1, 10):
    max_pq.insert(i)
    print(max_pq.mpq)
print("###")
print(max_pq.pop())
print(max_pq.mpq)
