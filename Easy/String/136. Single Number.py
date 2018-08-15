#First Version:
class Solution:
    def singleNumber(self, nums):
        dic = {}
        for num in nums:
            if str(num) not in dic:
                dic[str(num)] = 1
            else:
                dic.pop(str(num))
        return int(max(dic))

#Second Version:
class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

#Other solutions:
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)
    
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)
    
def singleNumber(self, nums):
    return reduce(operator.xor, nums)