class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)

        i=0
        j=len(nums)-1
        e=0
        f=k-1

        z=k
        x=len(nums)-1

        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        while e<f:
            nums[e],nums[f]=nums[f],nums[e]
            e+=1
            f-=1
        while z<x:
            nums[z],nums[x]=nums[x],nums[z]
            z+=1
            x-=1

                