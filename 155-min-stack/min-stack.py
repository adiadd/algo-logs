class MinStack:

    def __init__(self):
        self.store = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.store.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.store:
            if self.store[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.store.pop()
        

    def top(self) -> int:
        return self.store[-1] if self.store else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()