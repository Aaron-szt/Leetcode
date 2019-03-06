class Solution:
    def maxSubArray(self, nums):
        maxi = - 2 ** 31
        if len(nums) == 0:
            return None
        dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if i > 0:
                dp[i] += dp[i - 1] if dp[i - 1] > 0 else 0
            dp[i] += nums[i]
            if dp[i] > maxi:
                maxi = dp[i]
        return maxi