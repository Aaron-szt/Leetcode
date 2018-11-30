class Solution:
    def search(self, nums, target):        
        if target not in nums:
            return -1
        
        # prepare the ascending nums that include the target
        bia = 0
        new_nums = nums
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if nums[0] <= target:
                    new_nums = nums[:i]
                else:
                    new_nums = nums[i:]
                    bia = i
                break
            
                    
        # use binary search to find the target in an ascending array
        left = 0
        right = len(new_nums) - 1
        ans = 0
        while left <= right:
            mid = (right - left)//2 + left
            if new_nums[mid] == target:
                return mid + bia
            if new_nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1