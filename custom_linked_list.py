class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_head(self, e):
        node = Node(e)
        node.next = self.head
        self.head = node
        self.size += 1
    
    def add_tail(self,e):
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = Node(e)
        self.size += 1

    def find_third_to_last(self):
        ptr0 = self.head
        ptr1 = self.head.next.next
        while ptr1.next is not None:
            ptr0 = ptr0.next
            ptr1 = ptr1.next
        return ptr0
    
    def reverse(self):
        previousNode = None
        currentNode = self.head
        nextNode = self.head.next
        while currentNode is not None:
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
            if nextNode is not None: 
                nextNode = nextNode.next
        self.head = previousNode

    def toString(self):
        string = ""
        ptr = self.head
        while ptr is not None:
            string += str(ptr.data) + " "
            ptr = ptr.next
        return string

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def main():
    list = LinkedList()
    list.add_head(3)
    list.add_head(2)
    list.add_head(1)
    list.add_tail(4)
    list.add_tail(5)
    print("\nList before reversal: ", list.toString())
    print("Third to last element:", list.find_third_to_last().data, "\n")
    
    list.reverse()
    print("List after reversal:  ", list.toString())
    print("Third to last element:", list.find_third_to_last().data, "\n")


if __name__ == "__main__":
        main()