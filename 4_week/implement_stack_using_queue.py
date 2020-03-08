from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.appendleft(x)
        for _ in range(len(self.q) - 1):
            self.q.appendleft(self.q.pop())

    def pop(self):
        return self.q.pop()

    def top(self):
        return self.q[-1]

    def empty(self):
        return not self.q

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

