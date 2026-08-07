class MyQueue:

    def __init__(self):
        self.s=[]
        self.g=[]
        

    def push(self, x: int) -> None:
        self.s.append(x)
    def pop(self) -> int:
        if not self.g:
            while self.s:
                self.g.append(self.s.pop())   
        return self.g.pop()
    def peek(self) -> int:
        if not self.g:
            while self.s:
                self.g.append(self.s.pop())
        return self.g[-1]
        

    def empty(self) -> bool:
        return len(self.g)==0 and len(self.s)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()