class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a={}

        for i  in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]]=1
            else:
                return nums[i]
        