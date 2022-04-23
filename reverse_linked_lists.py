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

    def link_iter(self):
        current = self.head.next
        while current is not None:
            print(current.data)
            current = current.next


class Reverser(object):
    def __init__(self, ll):
        self.ll = ll

    def reverse(self):
        head = self.ll.head
        if head.next is None:
            return self.ll
        elif head.next.next is None:
            return self.ll
        else:
            curr = head.next
            pred = curr.next
            head.next = None
            hold = head.next

            while pred is not None:
                head.next = curr
                curr = pred
                pred = pred.next
                head.next.next = hold
                hold = head.next

            head.next = curr
            curr.next = hold
            return self.ll



l1 = LinkedList(Node('inf'))
node = Node(1)
l1.head.next = node
l1.head.next.next = Node(2)
l1.head.next.next.next = Node(3)
l1.head.next.next.next.next = Node(4)

l1.link_iter()
print()
Reverser(l1).reverse()
l1.link_iter()
