from collections import deque

class MyQueue:

    def __init__(self):
        self.load_stack = deque() 

    def push(self, x: int) -> None:
        self.load_stack.append(x)

    def pop(self) -> int:
        return self.load_stack.popleft()

    def peek(self) -> int:
        return self.load_stack[0]

    def empty(self) -> bool:
        return not self.load_stack
    

m = MyQueue()
m.push(1)
m.push(2)
print(m.pop())
        
