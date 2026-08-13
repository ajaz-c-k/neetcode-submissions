class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        for token in tokens:
            if token not in ["+","-","/","*"]:
                a.append(int(token))
            elif token=="+":
                b=a.pop()
                s=a.pop()
                ans=b+s
                a.append(ans)
            elif token=="*":
                b=a.pop()
                s=a.pop()
                ans=b*s
                a.append(ans)
            elif token=="-":
                b=a.pop()
                s=a.pop()
                ans=s-b
                a.append(ans)
            elif token=="/":
                b=a.pop()
                s=a.pop()
                ans=s/b
                a.append(int(ans))
        n=a.pop()
        return int(n)
