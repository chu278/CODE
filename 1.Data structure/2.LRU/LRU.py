# put 和 get 方法的时间复杂度为 O(1)，我们可以总结出 cache 这个数据结构必要的条件：
#                                         查找快，插入快，删除快，有顺序之分。
# 哈希表查找快，但是数据无固定顺序；链表有顺序之分，插入删除快，但是查找慢。
# 所以结合一下，形成一种新的数据结构：哈希链表。


class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.pre = None


class NodeList:
    def __init__(self):
        self.length = 0
        self.head = Node(0, 0)
        self.rear = Node(0, 0)
        self.head.next = self.rear
        self.head.pre = None
        self.rear.next = None
        self.rear.pre = self.head

    def add_node(self, node: Node):
        tmp = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = tmp
        tmp.pre = node
        self.length += 1

    def remove(self, node: Node):
        remove_node = node
        tmp_next = node.next
        tmp_pre = node.pre
        tmp_pre.next = tmp_next
        tmp_next.pre = tmp_pre
        self.length -= 1
        return remove_node

    def remove_last(self):
        # length > 0
        tmp = self.rear.pre.pre
        remove_node = self.rear.pre
        self.rear.pre = tmp
        tmp.next = self.rear
        self.length -= 1
        return remove_node

    def show_length(self):
        return self.length

    def show_rear(self):
        tmp = self.rear.pre
        print("Rear->Head", end=" ")
        while tmp != self.head and tmp is not None:
            print((tmp.key, tmp.value), end=" ")
            tmp = tmp.pre
        print("")

    def show_head(self):
        tmp = self.head.next
        print("Head->Rear", end=" ")
        while tmp != self.rear and tmp is not None:
            print((tmp.key, tmp.value), end=" ")
            tmp = tmp.next
        print("")


class LRU:
    def __init__(self, cap):
        self.lru_map: {int: Node} = {}
        self.cap = cap
        self.node_list = NodeList()

    def get(self, k):
        if k not in self.lru_map.keys():
            # 把旧的数据删除；将新节点 x 插入到开头；
            return -1
        else:
            v = self.lru_map[k].value
            self.put(k, v)
            return v

    def put(self, k, v):
        node = Node(k, v)
        if k in self.lru_map.keys():
            self.node_list.remove(self.lru_map.get(k))
            self.node_list.add_node(node)
            self.lru_map[k] = node
        else:
            if self.cap == len(self.lru_map):
                last = self.node_list.remove_last()
                self.lru_map.pop(last.key)
            self.node_list.add_node(node)
            self.lru_map[k] = node


# nl = NodeList()
# for i in range(1, 11):
#     nl.add_node(Node(i, i))
# nl.show_rear()
# nl.show_head()
# print(nl.show_length())
# remove = nl.remove_last()
# print(remove.key, remove.value)
# nl.show_rear()
# nl.show_head()
# print(nl.show_length())

lru = LRU(4)
for i in range(9):
    lru.put(i, i)
lru.get(5)
print(lru.lru_map)
lru.node_list.show_head()
