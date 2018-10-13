class Solution:
    def findLengthOfLCIS(self, nums):
        if nums == []:
            return 0
        ans = 1
        maxi = 1
        mini = nums[0]
        for i in range(len(nums)):
            if nums[i] > mini:
                maxi += 1
                ans = max(ans, maxi)
                mini = nums[i]
            else:
                maxi = 1
                mini = nums[i]
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        