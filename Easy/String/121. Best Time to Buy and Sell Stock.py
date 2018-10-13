class Solution:
    def maxProfit(self, prices):
        maxCur = 0
        maxSoFar = 0
        i = 1
        while i < len(prices):
            maxCur = max(0, maxCur + prices[i] - prices[i-1])
            maxSoFar = max(maxSoFar, maxCur)
            i += 1
        return maxSoFar

#  class Solution:
#     def binaryTreePaths(self, root):
#         if prices == [] or len(prices) == 1: return 0
#         maxPro = 0
#         minNum = prices[0]
#         for i in range(len(prices)):
#             if prices[i] > minNum:
#                 maxPro = max(maxPro, prices[i] - minNum)
#             else:
#                 minNum = prices[i]
                    
#         return maxPro

# class Solution:
#     def maxProfit(self, prices):
#         if prices == [] or len(prices) == 1: return 0
#         l, r = 0, len(prices) - 1
#         while prices[l] >= prices[l+1]:
#             l += 1
#             if l == r: return 0
#         while prices[r-1] >= prices[r]:
#             r -= 1
#             if l == r: return 0
#         maxPro = 0
#         for i in range(l, r+1):
#             for j in range(i+1, r+1):
#                 if prices[j] - prices[i] > maxPro:
#                     maxPro = prices[j] - prices[i]
                    
#         return maxPro