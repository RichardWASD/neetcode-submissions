class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r, profit = 0,1,0;
        # profit= prices[r]-prices[l]
        while (l<r and r < len(prices)):
            diff = prices[r]-prices[l];

            if(diff > profit):
                profit = diff;

            if(prices[l] > prices[r]):
                l = r
            
            r+=1;

        return profit;

