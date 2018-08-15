class Solution:
    def reverseString(self, s):
        max_index = len(s)-1        
        result = ""
        for index,value in enumerate(s):
            result += s[max_index-index]
        return result

#解法2:
#class Solution:
#    def reverseString(self, s):
#        result=s[::-1]
#        return result