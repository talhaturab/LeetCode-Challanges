from inspect import stack


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(self.stack)

    def pop(self) -> None:
        del self.stack[-1]
        print(self.stack)

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        min = self.stack[0]
        for element in self.stack:
            if element < min:
                min = element
        return min

x = MinStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
x.pop()
print(x.top())
print(x.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()