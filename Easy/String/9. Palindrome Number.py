class Solution:
    def isPalindrome(self, x):
        a = list(str(x))
        for i in range((len(a)+1)//2):
            if a[i] != a[len(a)-i-1]:
                return False
        return True

#一行版本：
class Solution:
    def isPalindrome(self, x):
        return int(str(abs(x))[::-1])==x