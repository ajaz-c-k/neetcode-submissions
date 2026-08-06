class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        for i in range(len(operations)):
            if operations[i]=="C":
                a.pop()
            elif operations[i]=="D":
                a.append(a[-1]*2)
            elif operations[i]=="+":
                ad=a[-1]+a[-2]
                a.append(ad)
            else:
                a.append(int(operations[i]))
        sums=0

        total=sum(a)

        return total



        