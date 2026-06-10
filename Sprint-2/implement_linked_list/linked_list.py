
class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self, value):
        node = LinkedList.Node(value)
        if self.head is not None:
            node.next = self.head
            self.head.previous = node
        else:
            self.tail = node
        self.head = node
        return node
