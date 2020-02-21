class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.hashset = [None] * self.size

    def add(self, key: int) -> None:
        """
        Add key to hashset
        :param key: int
        :return: None
        """
        hashkey = hash(key) % self.size
        if not self.hashset[hashkey]:
            self.hashset[hashkey] = Node(key)
        else:
            node = self.hashset[hashkey]
            if node.value == key: return
            while node.next and node.value != key:
                node = node.next
            if node.value != key:
                node.next = Node(key)

    def remove(self, key: int) -> None:
        if not self.contains(key): return
        hashkey = hash(key) % self.size
        node = self.hashset[hashkey]
        if node.value == key:
            self.hashset[hashkey] = node.next
            return
        while node.next.value != key:
            node = node.next
        node.next = node.next.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashkey = hash(key) % self.size
        if not self.hashset[hashkey]:
            return False
        node = self.hashset[hashkey]
        while node:
            if node.value == key:
                return True
            node = node.next
        return False