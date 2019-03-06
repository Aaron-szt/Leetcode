class Solution:
    def judgeSquareSum(self, c):
        if c == 0:
            return True
        for i in range(c):
            if i*i > c:
                return False
            j = int((c - i*i) ** 0.5)
            if j*j + i*i == c:
                return True
        """
        :type c: int
        :rtype: bool
        """
        