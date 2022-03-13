class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack:
            for element in self.stack:
                if val <= element:
                    index = self.stack.index(element)
                    self.stack.insert(index, val)
                    print(self.stack)
                    return
            self.stack.append(val)
        else:
            self.stack.append(val)
        print(self.stack)

    def pop(self) -> None:
        del self.stack[-1]
        print(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()