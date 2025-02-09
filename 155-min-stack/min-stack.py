class MinStack:

    def __init__(self):
        self.store = []

    def push(self, val: int) -> None:
        self.store.append(val)

    def pop(self) -> None:
        del self.store[-1]

    def top(self) -> int:
        return self.store[-1]

    def getMin(self) -> int:
        return min(self.store)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()