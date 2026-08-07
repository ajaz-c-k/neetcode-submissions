class MinStack:

    def __init__(self):
        self.g=[]
        self.m=[]
        

    def push(self, val: int) -> None:
        self.g.append(val)
        if not  self.m:
            self.m.append(val)
        else:
            self.m.append(min(val,self.m[-1]))
        

    def pop(self) -> None:
        self.g.pop()
        self.m.pop()
        

    def top(self) -> int:
        a=self.g[-1]
        return a
        

    def getMin(self) -> int:
        return self.m[-1]
