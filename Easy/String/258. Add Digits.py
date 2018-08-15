class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            temp = 0
            while num > 0:
                temp += num%10
                num //= 10
            num = temp
        return num
            
#Orz
class Solution(object):
def addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """
    if num == 0 : return 0
    else:return (num - 1) % 9 + 1