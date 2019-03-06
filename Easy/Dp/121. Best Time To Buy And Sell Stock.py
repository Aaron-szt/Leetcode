class Solution:
    def maxProfit(self, prices):
        maxi = 0
        new_prices = []
        if len(prices) <= 1:
            return 0
        for i in range(1, len(prices)):
            new_prices.append(prices[i] - prices[i-1])
        
        dp = [0] * len(prices)
        for i in range(len(new_prices)):
            if i > 0:
                dp[i] += dp[i-1] if dp[i-1] > 0 else 0
            dp[i] += new_prices[i]
            if dp[i] > maxi:
                maxi = dp[i]
        return maxi
        """
        :type prices: List[int]
        :rtype: int
        """
        