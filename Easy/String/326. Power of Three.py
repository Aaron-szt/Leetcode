class Solution:
    def isPowerOfThree(self, n):
        while n % 3 == 0 and n != 0:
            n = n / 3
        if n == 1:
            return True
        else:
            return False