class Solution:
    def moveZeroes(self, nums):
        i = 0
        count = 0
        while i < len(nums) and count < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                i -= 1
                count += 1
                nums.append(0)
            i += 1
            
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        