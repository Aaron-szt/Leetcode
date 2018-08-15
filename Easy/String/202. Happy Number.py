class Solution:
    def isHappy(self, n):
        mem = set()
        while n != 1:
            n = sum(int(num) ** 2 for num in str(n))
            if n not in mem:
                mem.add(n)
            else:
                return False
        else:
            return True

#本来想搞的直接手写出来然后查字典……
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    happySet = set([1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97])
    while n>99:
        n = digitSquareSum(n)
    return n in happySet