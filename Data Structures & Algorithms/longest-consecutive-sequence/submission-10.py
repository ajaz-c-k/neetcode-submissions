class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        if not nums:
            return 0
        maximum=1
        for num in nums:
            if num-1 not in s:
                current=num
                length=1
                while current+1 in s:
                    length+=1
                    current+=1
                maximum=max(maximum,length)

        return maximum
                
