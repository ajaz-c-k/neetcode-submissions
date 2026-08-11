class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        seen={}
        max_length=0
        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]]=r
            else:
                l=max(l,seen[s[r]]+1)
                seen[s[r]]=r

            current_max=r-l+1
            max_length=max(max_length,current_max)

        return max_length

                

        