class Solution:
    def isValid(self, s: str) -> bool:
        symbol=[]
        pairs={
            ')':'(',
            '}':'{',
            ']':'[',
        }

        for c in s:
            if c in "{([":
                symbol.append(c)
            else:
                need=pairs[c]
                if not symbol:
                    return False
                if need != symbol[-1]:
                    return False
                symbol.pop()
        return len(symbol)==0


        