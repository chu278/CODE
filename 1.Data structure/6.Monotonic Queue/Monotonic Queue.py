from collections import deque


class MQ:
    def __init__(self, k):
        self.queue = deque()
        self.result = []
        self.window_size = k

    def push(self, n):
        while len(self.queue) != 0:
            right = self.queue.pop()
            if right >= n:
                self.queue.append(right)
                break
        self.queue.append(n)

    def max_data(self):
        left = self.queue.popleft()
        self.queue.appendleft(left)
        return left

    def pop(self, n):
        if len(self.queue) != 0:
            left = self.queue.popleft()
            if left != n:
                self.queue.appendleft(left)
        # if len(self.queue) == 3:
        #     self.queue.popleft()

    def max_sliding_window(self, nums):
        for i in range(len(nums)):
            if i < self.window_size - 1:
                self.push(nums[i])
            else:
                self.push(nums[i])
                self.result.append(self.max_data())
                self.pop(nums[i - self.window_size + 1])
        return self.result


mq = MQ(4)
print(mq.max_sliding_window([-7,-8,7,5,7,1,6,0]))
# [3, 3, 3, 5, 5, 6, 7]