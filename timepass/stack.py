class Stack:
    def __init__(self, maxSize) -> None:
        self.n = maxSize
        self.stack = [] * self.n
    
    def push(self, val) -> None:
        if len(self.stack) > self.n:
            print("Stack is overflowing")
            return
        
        self.stack.append(val)

    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

    def peek(self) -> int:
        if not self.stack:
            print("Stack empty")
            return
        return self.stack[-1] 
    
    def printStack(self) -> None:
        if not self.stack:
            print("Empty stack")
            return
        print(self.stack)
        
if __name__ == "__main__":
    stack = Stack(5)
    stack.printStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.printStack()
    val = stack.pop()
    print(f"Popped is {val}" )
    print(f"Top of the stack is: {stack.peek()}")
    
    