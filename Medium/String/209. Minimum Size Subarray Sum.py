class Solution:
    def minSubArrayLen(self, s, nums):
        if sum(nums) < s:
            return 0
        fast = 0
        slow = 0
        tsum = nums[0]
        ans = len(nums)
        while fast < len(nums):
            while tsum < s and fast < len(nums) - 1:
                fast += 1
                tsum += nums[fast]
            while tsum >= s and slow <= fast:
                tsum -= nums[slow]
                slow += 1
            slow -= 1
            tsum += nums[slow]
            ans = min(ans, fast - slow + 1)
            fast += 1
            if fast < len(nums):
                tsum += nums[fast]
        return ans