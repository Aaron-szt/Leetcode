class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j+1 < k and nums[j] == nums[j-1]:
                        j += 1
                    while k-1 >= j and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return ans