class SinglyList:
    class _Node:
        def init(self, e, next):
            self._element = e
            self._next = next

    def init(self):
        self._head = self._tail = None

    def find_median(self):
        slow = self._head
        fast = self._head
        while (fast != None and fast._next != None):
            slow = slow._next
            fast = fast._next._next
        return slow._element

