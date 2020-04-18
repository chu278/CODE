from queue import Queue


class Stack2Queue:
    def __init__(self):
        self.q = Queue()
        self.top = None
        self.size = 0

    def stack_push(self, element):
        self.q.put(element)
        self.top = element
        self.size += 1

    def stack_pop(self):
        if self.stack_empty():
            return
        # 纪录top元素值并且更新top值
        tmp = 1
        while tmp < self.size:
            data = self.q.get()
            self.q.put(data)
            # 之前队列中最后元素之前一个元素作为新的top
            if tmp == self.size - 1:
                self.top = data
            tmp += 1
        data = self.q.get()
        self.size -= 1
        if self.stack_empty():
            self.top = None
        return data

    def stack_empty(self):
        if self.q.empty():
            return True
        return False

    def stack_top(self):
        return self.top

    def show(self):
        while not self.q.empty():
            print(self.q.get(), end=" ")
        print("")
        self.size = 0


s2q = Stack2Queue()
s2q.stack_push(1)
s2q.stack_push(2)
s2q.stack_push(3)
s2q.stack_push(4)
s2q.stack_push(5)
s2q.show()

s2q.stack_push(1)
s2q.stack_push(2)

print(s2q.stack_pop())
print(s2q.top)

s2q.show()
