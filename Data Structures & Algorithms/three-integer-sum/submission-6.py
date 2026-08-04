class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if nums[i]==nums[i-1] and i >0:
                continue
            fixed=nums[i]
            left=i+1
            right=len(nums)-1
            
            while left<right:
                a=fixed+nums[left]+nums[right]
                if a==0:
                    ans.append([fixed,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif a>0:
                    right-=1
                else:
                    left +=1
        return ans