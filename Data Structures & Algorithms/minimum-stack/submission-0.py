class MinStack:

    def __init__(self):
        self.g=[]
        

    def push(self, val: int) -> None:
        self.g.append(val)
        

    def pop(self) -> None:
        self.g.pop()
        

    def top(self) -> int:
        a=self.g[-1]
        return a
        

    def getMin(self) -> int:
        f=min(self.g)
        return f
