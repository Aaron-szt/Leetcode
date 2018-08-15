#卧槽一遍过了开心
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        l = []
        count = 32
        result = 0
        while count != 0:
            if n != 0:
            	l.append(n % 2)
            	n = n // 2
            else:
            	l.append(0)
            count -= 1
        for i in range(32):
        	result += l[i] * 2 ** (31-i)
        return result

#Pythonic code:
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)