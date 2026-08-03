class Solution:
    def validPalindrome(self, s: str) -> bool:
        clean=""
        for char in s:
            if char.isalnum():
                clean=clean+char.lower()
        
        i=0
        j=len(clean)-1
        def isPalindrome(left,right):
            while left<right:
                if clean[left]==clean[right]:
                    left+=1
                    right-=1
                    
                else:
                    return False
            return True

        while i<j:
            if clean[i]==clean[j]:
                i+=1
                j-=1
            else:
                return isPalindrome(i+1,j) or isPalindrome(i,j-1)
        return True

        


        