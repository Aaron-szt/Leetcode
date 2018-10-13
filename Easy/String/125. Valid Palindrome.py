class Solution:
    def isPalindrome(self, s):
        snew = s.lower()
        left = 0
        right = len(snew) - 1
        while left < right:
            while not 48 <= ord(snew[left]) <= 57 and not 97 <= ord(snew[left]) <= 122 and left < right: left += 1
            while not 48 <= ord(snew[right]) <= 57 and not 97 <= ord(snew[right]) <= 122 and left < right: right -= 1  
            if snew[left] == snew[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    
#         i = 0
#         s = s.lower()
#         snew = []
#         while i < len(s):
#             if 48 <= ord(s[i]) <= 57 or 97 <= ord(s[i]) <= 122:
#                 snew.append(s[i]) 
#             i += 1
        
#         left = 0
#         right = len(snew) - 1
#         while left < right:
#             if snew[left] == snew[right]:
#                 left += 1
#                 right -= 1
#             else:
#                 return False
#         return True