class MinStack:

    def __init__(self):
        # Initialize two stacks; one to hold the actual stack values,
        # and the other to keep track of the minimum value at any given point.
        self.stack = []
        self.min_stack = [float('inf')]  # Initialize with infinity to handle edge case for the first element pushed

    def push(self, val: int) -> None:
        # Add the value to the main stack
        self.stack.append(val)
        # Add the minimum value to the min_stack which is the minimum of the new value and the current minimum
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:

        # Remove the top value from both main stack and min_stack
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the top value of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the current minimum value which is the top value of the min_stack
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_4 = obj.getMin()

print(obj.min_stack)
print(param_4)
obj.pop()
print(obj.top())
print(obj.getMin())