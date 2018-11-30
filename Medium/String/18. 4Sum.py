class Solution:
    def fourSum(self, nums, target):
        
        def nSum(start, end, target, n, tmp, ans):
            if n < 2 or end - start + 1 < n:
                return ans
            if n == 2:
                l, r = start, end
                while l < r:
                    if nums[l] + nums[r] == target:
                        ans.append(tmp + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l+1 < r and nums[l] == nums[l-1]:
                            l += 1
                        while r-1 >= l and nums[r] == nums[r+1]:
                            r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
                return ans
            
            else:
                for i in range(start, end):
                    if i-start > 0 and nums[i] == nums[i-1]:
                        continue
                    if target >= n * nums[i] and target <= n * nums[end]:
                        tmp.append(nums[i])
                        ans = nSum(i+1, end, target-nums[i], n-1, tmp, ans)
                        tmp.remove(nums[i])
            return ans
                
        nums.sort()
        ans = []
        ans = nSum(0, len(nums)-1, target, 4, [], ans)
        print(nums)
        return ans
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        