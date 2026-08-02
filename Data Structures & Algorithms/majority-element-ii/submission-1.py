class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c={}

        for num in nums:
            if  num not in c:
                c[num]=1
            else:
                c[num]+=1
        a=[]
        for i,j in c.items():
            if j>len(nums)//3:
                a.append(i)
        return a