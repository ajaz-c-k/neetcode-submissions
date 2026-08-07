class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={0:1}
        current_prefix=0
        count=0
        

        for num in nums:
            current_prefix=current_prefix+num
            needed=current_prefix-k

            if needed in a:
                count+=a[needed]
            
            if current_prefix in a:
                a[current_prefix]+=1
            else:
                a[current_prefix]=1
        return count
            

            

            
            
