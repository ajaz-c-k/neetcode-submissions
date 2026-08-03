class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write=0
        read=1

        for read in range(1,len(nums)):
            if nums[write]==nums[read]:
                read=read+1
            else:
                write=write+1
                nums[write]=nums[read]
                read=read+1
        k=write +1
        return k
            