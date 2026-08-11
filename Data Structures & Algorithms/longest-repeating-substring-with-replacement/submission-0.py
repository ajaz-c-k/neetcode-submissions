class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        seen={}
        maximum_length=0

        for right in range(len(s)):
            if s[right] not in seen:
                seen[s[right]]=1
            else:
                seen[s[right]]+=1
            max_count=max(seen.values())
            window_size=right-left+1
            replacement_needed=window_size-max_count  

            if replacement_needed>k:  
                seen[s[left]]-=1    
                left=left+1
            window_size=right-left+1
            maximum_length=max(maximum_length,window_size) 
        return maximum_length
            


        