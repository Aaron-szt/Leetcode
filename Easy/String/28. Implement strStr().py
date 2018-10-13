class Solution:
    def strStr(self, haystack, needle):
        # if haystack == needle or needle == '':
        #     return 0
        # else:
        #     i = 0
        #     dic = {}
        #     while i < len(haystack) - len(needle) + 1:
        #         if needle in dic:
        #             return dic[needle]
        #         else:
        #             dic[haystack[i:i+len(needle)]] = i
        #         i += 1
        #     if needle in dic:
        #         return dic[needle]
        #     print(dic)
        #     return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
        
        
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        