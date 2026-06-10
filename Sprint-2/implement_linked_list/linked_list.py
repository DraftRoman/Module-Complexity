
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

    def pop_tail(self):
        if self.tail is None:
            raise IndexError("pop from empty list")
        value = self.tail.value
        if self.tail.previous is not None:
            self.tail.previous.next = None
        else:
            self.head = None
        self.tail = self.tail.previous
        return value

    def remove(self, node):
        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous