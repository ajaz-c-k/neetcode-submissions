class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        a=[]
        for i in range(len(numbers)):
            if numbers[left]+numbers[right]==target:
                a.append(left+1)
                a.append(right+1)
                return list(a)
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1

        