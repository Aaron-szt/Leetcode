class Solution:
    def containsDuplicate(self, nums):
        s = set()
        if nums == []:
            return False
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                return True
        return False

#一行代码……Orz
class Solution:
    def containsDuplicate(self, nums):
    return len(nums) != len(set(nums))