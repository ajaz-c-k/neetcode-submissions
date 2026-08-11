class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        current_sum=0
        min_length=0
        for right in range(len(nums)):
            current_sum+=nums[right]
            while current_sum>=target:
                window_length=right-left+1
                if min_length==0:
                    min_length=window_length
                else:
                    min_length=min(min_length,window_length)
                current_sum-=nums[left]
                left=left+1
            
                
                
        return min_length


        