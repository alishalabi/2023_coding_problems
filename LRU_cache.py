"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
"""

# Key constraint: all keys are unique

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def replace_node(self, data):
        node = Node(data)
        self.head = self.head.next
        self.tail.next = node

    def increase_size(self):
        self.size += 1

class LRU:
    def __init__(self, capacity):
        self.LL = LinkedList()
        self.capacity = capacity
        self.references = {}

    def insert(self, data):
        if self.LL.size < self.capacity:
            self.LL.add_node(data)
            self.LL.increase_size()
            self.references.update({data[0]: data[1]})
        else:
            self.references.pop(self.LL.head.data[0])
            self.LL.replace_node(data)
            self.references.update({data[0]: data[1]})

    def contains(self, key):
        if key in self.references:
            return self.references[key]
        else:
            return None

example = LRU(2)
example.insert([1, "1 here"])
example.insert([2, "2 here"])
print(example.contains(1))
example.insert([3, "3 here"])
print(example.contains(1))
print(example.contains(3))
