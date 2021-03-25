# Most of this code is taken from Dr. Omari's example code posted on BB
# The functionality asked for in PP11 has been implemented on top of the existing code by Carter Burzlaff
# Testing code was added by Carter Burzlaff

class LinkedBinaryTree:
    class _Node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def height(self):
        return self._height(self._root)

    def _height(self, p):
        if not p:
            return 0
        return 1 + max(self._height(p._left), self._height(p._right))

    def in_order(self):
        for e in self._in_order(self._root):
            yield e

    def _in_order(self, p):
        if p is not None:
            for other in self._in_order(p._left):
                yield other

            yield p._element
            for other in self._in_order(p._right):
                yield other


# NEW IMPLEMENTED METHODS FOR PP11
    def _insert(self, key, p):
        if not p:
            new_node = self._Node(key)
            return new_node
        if key < p._element:
            p._left = self._insert(key, p._left)
        else:
            p._right = self._insert(key, p._right)
        return p
    
    def insert(self, key):
        if not self._root:
            self._root = self._Node(key)
        else:
            self._insert(key, self._root)
    
    def search(self, key):
        p = self._root
        while p is not None:
            if p._element == key:
                return True
            elif key < p._element:
                p = p._left
            else:
                p = p._right
        return False

    def print_in_order(self):
        for e in self._in_order(self._root):
            print(e)

print("-------BEGINNING TESTING OF DEMO TREE---------")
tree = LinkedBinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(6)
tree.insert(4)
tree.insert(8)
tree.insert(2)
print("5 is in this tree:", tree.search(5))
print("1 is in this tree:", tree.search(1))
print("The tree in order is:")
tree.print_in_order()

