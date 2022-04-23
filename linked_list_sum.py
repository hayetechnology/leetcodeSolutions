class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self, head):
        self.head = head
        self.head.next = None

    def append(self, n):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = n

    def iter(self):
        current = self.head.next
        while current is not None:
            print(current.data)
            current = current.next


class Solver(object):
    def __init__(self, l1, l2, l3, sum, n):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.sum = sum
        self.n = n

    def sum_lists(self):
        temp1 = l1.head.next
        temp2 = l2.head.next
        if temp1 is not None and temp2 is not None:
            self.sum = self.sum + ((temp1.data + temp2.data) * pow(10, self.n))
            l1.head.next = temp1.next
            l2.head.next = temp2.next
            self.n = self.n + 1
            self.sum_lists()
        elif temp1 is not None:
            self.sum = self.sum + (temp1.data * pow(10, self.n))
            l1.head.next = temp1.next
            self.n = self.n + 1
            self.sum_lists()
        elif temp2 is not None:
            self.sum = self.sum + (temp2.data * pow(10, self.n))
            l2.head.next = temp2.next
            self.n = self.n + 1
            self.sum_lists()
        else:
            sum_string = str(self.sum)

            sum_string = sum_string.split()
            size = len(sum_string)
            i = size - 1
            while i >= 0:
                digit = int(sum_string[i])
                i = i - 1
                node = Node(digit)
                l3.append(node)
            return l3


l1 = LinkedList(Node('inf'))
node = Node(102)
l1.head.next = node
#l1.head.next.next = Node(2)
#l1.head.next.next.next = Node(2)

l2 = LinkedList(Node('inf'))
node2 = Node(8)
l2.head.next = node2
l2.head.next.next = Node(9)
l2.head.next.next.next = Node(9)

l3 = LinkedList(Node('inf'))

Solver(l1, l2, l3, 0, 0).sum_lists()

l3.iter()
