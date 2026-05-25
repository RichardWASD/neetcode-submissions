class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1
        # [10,1,5,6,7,1]
        #  ^    ^


        while(r < len(prices)):

            if(prices[l] < prices[r]): # condition to do calc
               potential_max = prices[r] -prices[l] 
               max_profit = max(max_profit, potential_max )
            else:
                l = r
            
            r += 1

        return max_profit