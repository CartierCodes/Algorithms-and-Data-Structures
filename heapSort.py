# A majority of this code is taken from example code posted by Dr. Omari
# The test code was created by Carter Burzlaff
# The timing and list generation was added by Carter Burzlaff

import time
import random

class Heap:
    def __init__(self):
        self._heap = []

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _last_idx(self):
        return len(self._heap) - 1

    def _left(self, i):
        return i * 2 + 1

    def _right(self, i):
        return i * 2 + 2

    def _parent(self, i):
        return (i - 1) // 2

    def _has_left(self, i):
        return self._left(i) < len(self._heap)

    def _has_right(self, i):
        return self._right(i) < len(self._heap)

    def empty(self):
        return len(self._heap) == 0

    def add(self, key):
        self._heap.append(key)

        j = self._last_idx()

        while j > 0 and self._heap[j] < self._heap[self._parent(j)]:
            self._swap(j, self._parent(j))
            j = self._parent(j)


    def remove_min(self):
        if self.empty():
            raise Exception()

        self._swap(0, self._last_idx())
        result = self._heap[-1]
        self._heap.pop()

        # push new element down the heap
        j = 0
        while True:
            min = j
            if self._has_left(j) and self._heap[self._left(j)] < self._heap[min]:
                min = self._left(j)

            if self._has_right(j) and self._heap[self._right(j)] < self._heap[min]:
                min = self._right(j)

            if min == j:
                #found right location for min, break
                break

            self._swap(j, min)
            j = min

        return result


def heap_sort(list):
    heap = Heap()
    for e in list:
        heap.add(e)
    sorted_list = []
    while not heap.empty():
        sorted_list.append(heap.remove_min())

    return sorted_list

# Basic insertion sort method
def insertion_sort(list):
    sorted_list = list
    for i in range(1, len(sorted_list)): 
        e = sorted_list[i] 
        j = i-1
        while j >= 0 and e < sorted_list[j]: 
            sorted_list[j+1] = sorted_list[j] 
            j -= 1
        sorted_list[j+1] = e
    return sorted_list


list = []
for i in range(0, 50): # filling the list with these numbers repeated 20 times
    list.append(random.randint(0, 100))

# test heap sorting
start = time.time()
print("\nHeap sorted list:\n", heap_sort(list))
heapTimeTaken = time.time() - start
print("Heap sort elapsed time: ", round(heapTimeTaken, 9), "s\n")

# test insertion sorting
start = time.time()
print("Insertion sorted list:\n", insertion_sort(list))
insertionTimeTaken = time.time() - start
print("Insertion sort elapsed time: ", round(insertionTimeTaken, 9), "s")

# print results
print("\nInsertion sort was faster by: ", round(insertionTimeTaken / heapTimeTaken, 7), "%")