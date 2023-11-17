from node import Node


class _BinTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self._root = None
        self._size = 0

    def height(self, subtree):
        if subtree is None:
            return -1
        else:
            hleft = self.height(subtree.left)
            hright = self.height(subtree.right)
            if hleft < hright:
                return hright + 1
            else:
                return hleft + 1

    def _search(self, subtree, value):
        if subtree is None:
            return None
        elif value < subtree.key:
            return self._search(subtree.left, value)
        elif value > subtree.key:
            return self._search(subtree.right, value)
        else:
            return subtree

    def _min(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._min(subtree.left)

    def _max(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._max(subtree.right)

    def _insert(self, subtree, value):
        if subtree is None:
            subtree = Node(value)
        elif value < subtree.key:
            subtree.left = self._insert(subtree.left, value)
        elif value > subtree.key:
            subtree.right = self._insert(subtree.right, value)
        return subtree

    def add(self, value):
        node = self._search(self._root, value)
        if node is None:
            self._root = self._insert(self._root, value)
            self._size += 1
            return True
        else:
            return False

    def _remove(self, subtree, target):
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self._remove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self._remove(subtree.right, target)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                sucessor = self._min(subtree.right)
                subtree.key = sucessor.key
                subtree.right = self._remove(subtree.right, sucessor.key)
                return subtree

    def remove(self, key):
        if self._search(self._root, key) is not None:
            self._root = self._remove(self._root, key)
            self._size -= 1
        else:
            print(f"\nChave {key} não encontrada.")


root = _BinTreeNode(60)
