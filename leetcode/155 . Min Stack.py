class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
        
obj = MinStack()

obj.push(-2)
print("Stack:", obj.stack)
print("Min Stack:", obj.min_stack)

obj.push(0)
print("Stack:", obj.stack)
print("Min Stack:", obj.min_stack)

obj.push(-3)
print("Stack:", obj.stack)
print("Min Stack:", obj.min_stack)

print("getMin() =", obj.getMin())

obj.pop()
print("After pop")
print("Stack:", obj.stack)
print("Min Stack:", obj.min_stack)

print("top() =", obj.top())
print("getMin() =", obj.getMin())