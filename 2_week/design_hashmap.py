class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 5000
        self.map = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = hash(key) % self.size
        node = prev = self.map[idx]
        if not node:
            self.map[idx] = Node(key, value)
            return
        while node:
            if node.key == key:
                node.value = value
                return
            prev, node = node, node.next
        prev.next = Node(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = hash(key) % self.size
        node = self.map[idx]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        node = prev = self.map[idx]
        if not node: return
        if node.key == key:
            self.map[idx] = node.next
        while node:
            if node.key == key:
                prev.next = node.next
            prev, node = node, node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)