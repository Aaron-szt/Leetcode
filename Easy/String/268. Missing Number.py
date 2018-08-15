class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        s = (n ** 2 + n) / 2
        return int(s - sum(nums))

#Yeah!!! This solution is among the best solutions~