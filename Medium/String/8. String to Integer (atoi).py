class Solution:
    def myAtoi(self, str):
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - 2 ** 31
        num = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '0':0}
        ans = ''
        flag = False
        i = 0
        while i < len(str):
            if str[i] == ' ':
                i += 1
                continue
            elif str[i] == '+' or str[i] == '-' or str[i] in num:
                ans += str[i]
                i += 1
                while i < len(str) and str[i] in num:
                    ans += str[i]
                    i += 1
                break
            else:
                break
        
        if ans == '':
            return 0
        if ans == '+' or ans == '-':
            return 0
        if int(ans) > INT_MAX:
            return INT_MAX
        if int(ans) < INT_MIN:
            return INT_MIN
        
        return int(ans)
            
        
            
                
        
        """
        :type str: str
        :rtype: int
        """
        