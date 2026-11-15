class MinStack:

    def __init__(self):
        self.min_value = float('inf')
        self.minValueStack = []
        self.my_stack = []

    def push(self, val: int) -> None:
        self.min_value = min(self.min_value, val)
        self.minValueStack.append(self.min_value)
        self.my_stack.append(val)

    def pop(self) -> None:
        val = self.my_stack.pop()
        self.minValueStack.pop()
        if self.minValueStack:
            self.min_value = self.minValueStack[0]
        else:
            self.min_value = float('inf')
        return val
        

    def top(self) -> int:        
        return self.my_stack[-1]

    def getMin(self) -> int:
        return self.minValueStack[-1]
        
