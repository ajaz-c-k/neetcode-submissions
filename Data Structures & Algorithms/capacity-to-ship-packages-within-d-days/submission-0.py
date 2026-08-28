class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)

        while left<right:
            mid=(left+right)//2
            current_weight=0
            needed_day=1

            for w in weights:
                if current_weight+w<=mid:
                    current_weight+=w
                else:
                    needed_day+=1
                    current_weight=w

            if needed_day<=days:
                right=mid
            else:
                left=mid+1
        return left



        