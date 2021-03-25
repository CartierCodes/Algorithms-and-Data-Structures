# A majority of this code is taken from example code posted by Dr. Omari
# countK() and equal() were created by Carter Burzlaff
# Some testing elements were added by Carter Burzlaff

class BinaryTree:
    class _Node:
        def __init__(self, e, left = None, right = None):
            self._left = left
            self._right = right
            self._element = e

    def __init__(self):
        self._root = None
        self._size = 0

    def is_empty(self):
        return self._root == None

    def add_root(self, e):
        if self._root:
            return None

        self._root = self._Node(e)
        return self._root

    def add_left(self, e, p):
        p._left = self._Node(e)
        return p._left

    def add_right(self, e, p):
        p._right = self._Node(e)

        return p._right

    def _height(self, v):
        if not v:
            return -1

        x = self._height(v._left)
        y = self._height(v._right)
        return 1 + max(x, y)

    def height(self):
        return self._height(self._root)

    def _inOrder(self, p):
        if p:
            for other in self._inOrder(p._left):
                yield other
            yield p._element
            for other in self._inOrder(p._right):
                yield other

    def inOrder(self):
        for e in self._inOrder(self._root):
            yield e

    def _preOrder(self, p):
        if p:
            print(p._elemet)
            self._preOrder(p._left)
            self._preOrder(p._right)

    def preOrder(self):
        self._preOrder(self._root)


    def _postOrder(self, p):
        if p:
            self._postOrder(p._left)
            self._postOrder(p._right)
            print(p._elemet)

    def postOrder(self):
        self._postOrder(self._root)

    def countK(self, num):
        counter = 0

        for e in self.inOrder():
            if e == num:
                counter += 1
        
        return counter

    def equal(self, other):
        returnValue = False
        if self.is_empty() and other.is_empty():
            returnValue = True

        stack1 = []
        stack2 = []
        for e in self.inOrder():
            stack1.append(e)
        for e in other.inOrder():
            stack2.append(e)
        if stack1 == stack2:
            returnValue = True

        return returnValue


# Original test code
bt = BinaryTree()
root = bt.add_root(10)
left_child = bt.add_left(5, root)
bt.add_right(7, root)

bt.add_left(8, left_child)
bt.add_right(2, left_child)

print(bt.height())


# Additional test code
print(bt.countK(10))
bt2 = bt
print(bt.equal(bt2))