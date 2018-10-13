class Solution(object):
    def change(self, amount, coins):
        dp = [0 for i in range(amount+1)]
        coinsKind = len(coins)
        dp[0] = 1
        for ck in range(coinsKind):
	        j = coins[ck]
	        while j <= amount:
		        dp[j] = (dp[j] + dp[j - coins[ck]])
		        j += 1
        return dp[amount]
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        