class Solution:
    def findMaxConsecutiveOnes(self, nums):
        res = 0
        temp = 0
        for n in nums:
            if n == 1:
                temp += 1
                if temp > res:
                    res = temp
            else:
                temp = 0
        return res
        