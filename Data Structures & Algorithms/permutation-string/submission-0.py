class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s={}
        word={}
        left=0

        for char in s1:
            if char not in s:
                s[char]=1
            else:
                s[char]+=1
        for right in range(len(s2)):
            if s2[right] not in word:
                word[s2[right]]=1
            else:
                word[s2[right]] += 1
            if right-left+1>len(s1):
                word[s2[left]]-=1
                if word[s2[left]] == 0:
                    del word[s2[left]]
                left+=1

            if word == s:
                return True
        return False


            
