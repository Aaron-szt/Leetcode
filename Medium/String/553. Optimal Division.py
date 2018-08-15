class Solution:
    def optimalDivision(self, nums):
        res = str(nums[0])
        if len(nums) == 1:
            return res
        elif len(nums) == 2:
            return res + "/" + str(nums[1])
        else:
            res += "/("
            for n in range(1, len(nums)):
                res = res + str(nums[n])
                if n != len(nums) - 1:
                    res = res + "/"
            res += ")"
        return res