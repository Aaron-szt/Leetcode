class Solution:
    def addBinary(self, a, b):
        ans = ""
        i, j, c = len(a)-1, len(b)-1, 0
        while i>=0 or j>=0 or c==1:
            c += ord(a[i])-ord('0') if i >= 0 else 0
            c += ord(b[j])-ord('0') if j >= 0 else 0
            ans = str(c % 2) + ans
            c = int(c / 2)
            i -= 1
            j -= 1
        
        return ans
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        