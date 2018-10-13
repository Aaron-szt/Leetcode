# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        def findFirst(left, right):
            mid = left + int((right - left + 1)/2)
            if left + 1 == right:
                self.ans = right
                return 1
            if isBadVersion(mid) is True:   findFirst(left, mid)
            else:   findFirst(mid, right)
        
        findFirst(0, n)
        return self.ans

# class Solution:
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         left = 0
#         right = n
#         while left < right - 1:
#             mid = left + int((right - left + 1)/2)
#             if isBadVersion(mid): right = mid
#             else: left = mid
        
#         return right
        