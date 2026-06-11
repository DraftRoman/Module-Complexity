import random


class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * level


class SkipList:

    MAX_LEVEL = 4

    def __init__(self):
        self.head = Node(-1, self.MAX_LEVEL)
        self.level = 1

    def random_level(self):

        level = 1

        while random.random() < 0.5 and level < self.MAX_LEVEL:
            level += 1

        return level

    def search(self, value):

        current = self.head

        for i in range(self.level - 1, -1, -1):

            while (
                current.forward[i]
                and current.forward[i].value < value
            ):
                current = current.forward[i]

        current = current.forward[0]

        return current is not None and current.value == value

    def insert(self, value):

        update = [None] * self.MAX_LEVEL
        current = self.head

        for i in range(self.level - 1, -1, -1):

            while (
                current.forward[i]
                and current.forward[i].value < value
            ):
                current = current.forward[i]

            update[i] = current

        new_level = self.random_level()

        if new_level > self.level:

            for i in range(self.level, new_level):
                update[i] = self.head

            self.level = new_level

        new_node = Node(value, new_level)

        for i in range(new_level):

            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def __contains__(self, value):
        return self.search(value)

    def to_list(self):

        result = []

        current = self.head.forward[0]

        while current:
            result.append(current.value)
            current = current.forward[0]

        return result