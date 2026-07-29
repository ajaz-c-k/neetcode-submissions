class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c={}
        count=0
        for num in nums:
            if num not in c:
                c[num]=1
            else:
                c[num]=c[num]+1
        
        for i,j in c.items():
            if j>len(nums)//2:
                return i

            
        