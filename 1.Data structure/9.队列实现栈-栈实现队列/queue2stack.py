import queue


class Queue2Stack:
    def __init__(self):
        # 类似栈 后入先出 last in first out
        self.s1 = queue.LifoQueue()
        self.s2 = queue.LifoQueue()

    def queue_empty(self):
        if self.s1.empty() and self.s2.empty():
            return True
        else:
            return False

    def queue_pop(self):
        self.peek()
        if self.s2.empty():
            return None
        return self.s2.get()

    def queue_push(self, v):
        self.s1.put(v)

    def show(self):
        pass

    def peek(self):
        if self.s2.empty():
            while not self.s1.empty():
                data = self.s1.get()
                self.s2.put(data)
        if self.s2.empty():
            return None
        data = self.s2.get()
        self.s2.put(data)
        return data


q2s = Queue2Stack()
for i in range(5):
    q2s.queue_push(i)

print(q2s.queue_pop())
print(q2s.queue_pop())

for i in range(5, 10):
    q2s.queue_push(i)

while not q2s.queue_empty():
    print(q2s.queue_pop())