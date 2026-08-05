class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        a=[]

        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if i>0 and nums[i-1]==nums[i]:
                    continue
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                fixed1=nums[i]
                fixed2=nums[j]
                left=j+1
                right=len(nums)-1
                while left<right:
                    f=fixed1+fixed2
                    k=nums[left]+nums[right]
                    if f+k==target:
                        a.append([fixed1,fixed2,nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif f+k>target:
                        right=right-1
                    else:
                        left=left+1
        return a





        
