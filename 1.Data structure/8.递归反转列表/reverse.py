# 递归反转链表的一部分
# 反转从位置m到n的链表，扫描一趟完成反转

class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class NodeList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.successor = None

    def insert(self, v):
        node = Node(v)
        if self.length == 0:
            self.head = node
            self.head.next = None
            self.length += 1
        else:
            node.next = self.head
            self.head = node
            self.length += 1

    def show(self, head):
        tmp = head
        while tmp is not None:
            print(tmp.value, end=" ")
            tmp = tmp.next
        print("")

    # 同级目录的递归反转列表.md文件中的网址讲解很容易理解
    def reverse_all(self, head: Node):
        if head.next is None:
            return head
        last = self.reverse_all(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverse_top_n(self, n, head):
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverse_top_n(n - 1, head.next)
        # 1->2->1
        head.next.next = head
        head.next = self.successor
        return last

    def reverse_between_m_n(self, m, n, head):
        if m == 1:
            return self.reverse_top_n(n, head)
        head.next = self.reverse_between_m_n(m - 1, n - 1, head.next)
        return head


node_list = NodeList()
node_list.insert(1)
node_list.insert(2)
node_list.insert(3)
node_list.insert(4)
node_list.insert(5)
node_list.show(node_list.head)
# new_head = node_list.reverse_all(node_list.head)
# node_list.show(new_head)

# new_head = node_list.reverse_top_n(3, node_list.head)
# node_list.show(new_head)

new_head = node_list.reverse_between_m_n(2, 3, node_list.head)
node_list.show(new_head)
