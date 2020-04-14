#  Next Greater Element
# 给你一个数组，返回一个等长的数组，对应索引存储着下一个更大元素，如果没有更大的元素，就存 -1。
# 给你一个数组 [2,1,2,4,3]，返回数组 [4,2,4,-1,-1]。
# 解释：
# 第一个 2 后面比 2 大的数是 4;
# 1 后面比 1 大的数是 2;
# 第二个 2 后面比 2 大的数是 4;
# 4 后面没有比 4 大的数，填 -1；
# 3 后面没有比 3 大的数，填 -1。


class MS:
    def __init__(self, data):
        self.stack = []
        self.data = data
        self.result = [-1] * len(self.data)

    def next_greater_element(self):
        for i in range(len(self.data)):
            while self.stack and self.data[self.stack[-1]] < self.data[i]:
                self.result[self.stack.pop()] = self.data[i]
            self.stack.append(i)
        return self.result

    # [2, 1, 2, 4, 3], 返回 [4, 2, 4, -1, 4]
    def next_greater_element_circle(self):
        for i in range(len(self.data) * 2):
            while self.stack and self.data[self.stack[-1]] < self.data[i % len(self.data)]:
                self.result[self.stack.pop()] = self.data[i % len(self.data)]
            self.stack.append(i % len(self.data))
        return self.result


ms = MS([2, 1, 2, 4, 3])
print(ms.next_greater_element())
ms = MS([2, 1, 2, 4, 3])
print(ms.next_greater_element_circle())
