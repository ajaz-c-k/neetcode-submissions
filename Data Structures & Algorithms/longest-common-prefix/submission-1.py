class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest=strs[0]
        for s in strs:
            if len(s)<len(shortest):
                shortest = s
        
        for i in range(len(shortest)):
            for j in strs:
                if shortest[i] != j[i]:
                    return shortest[:i]
        return shortest
        