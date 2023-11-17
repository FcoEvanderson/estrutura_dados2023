from queue import Queue


class _BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def pre_order(self, subtree):
        if subtree is not None:
            print(subtree.data)
            self.pre_order(subtree.left)
            self.pre_order(subtree.right)

    def in_order(self, subtree):
        if subtree is not None:
            self.in_order(subtree.left)
            print(subtree.data)
            self.in_order(subtree.right)

    def post_order(self, subtree):
        if subtree is not None:
            self.post_order(subtree.left)
            self.post_order(subtree.right)
            print(subtree.data)

    def breadthFirst(self, bintree):
        q = Queue()
        q.enqueue(bintree)
        while not q is None:
            node = q.dequeue()
            print(node.data)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

