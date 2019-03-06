class Solution:
    def permute(self, nums):
        def dfs(nums, ans, path):
            if not nums:
                ans.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], ans, path + [nums[i]])
        
        ans = []
        dfs(nums, ans, [])
        return ans