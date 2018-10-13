# 解法3:（124ms）
class Solution:
    def validPalindrome(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True


# 解法1:（1860ms）
# class Solution:
#     def validPalindrome(self, s):    
#         self.sa = ''
#         def isPali(ss):
#             while len(ss) > 1:
#                 if ss[0] == ss[-1]:
#                     ss = ss[1:-1]
#                 else:
#                     break
#             if len(ss) <= 1:
#                 return True
#             else:
#                 self.sa = ss
#                 return False
            
#         if isPali(s) is False:
#             saa = self.sa
#             return (isPali(saa[1:]) or isPali(saa[:-1]))
#         else:
#             return True


# 解法2:（240ms）
# class Solution:
#     def validPalindrome(self, s):
#         self.l, self.r = 0, 0
#         def isPali(ss, left, right):
#             while left < right:
#                 if ss[left] == ss[right]:
#                     left += 1
#                     right -= 1
#                 else: break
#             self.l, self.r = left, right
#             if (right-left+1)%2 == 1:
#                 return (right - left + 1 == 1)
#             else:
#                 return (right - left + 1 == 0)

#         if isPali(s, 0, len(s)-1) is False:
#             l, r = self.l, self.r
#             return (isPali(s, l+1, r) or isPali(s, l, r-1))
#         else:
#             return True