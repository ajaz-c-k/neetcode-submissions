class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_profit=0
        minimum=prices[0]
        

        for i in range(1,len(prices)):
            if prices[i]<minimum:
                minimum=prices[i]
            else:
                today_profit=prices[i]-minimum
                maximum_profit=max(today_profit,maximum_profit)
        return maximum_profit


            
        