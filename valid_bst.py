class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Validate(object):
    def is_valid_bst(self, lower_bound, n, upper_bound):
        if not n:
            return True
        val = n.val
        if ((lower_bound <= val <= upper_bound) and
                self.is_valid_bst(lower_bound, n.left, val) and
                self.is_valid_bst(val, n.right, upper_bound)):
            return True
        return False

    def is_valid(self, n):
        return self.is_valid_bst(float('-inf'), n, float('inf'))


node = Node(5)

node.right = Node(8)
node.right.left = Node(6)
#node.right.left.right = Node(9)
node.right.right = Node(10)

node.left = Node(2)
node.left.right = Node(3)
node.left.right.left = Node(0)
node.left.left = Node(1)


print(Validate().is_valid(node))
