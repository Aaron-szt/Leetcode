class Solution:
    def romanToInt(self, s):
        special = {'CD':400, 'CM':900, 'XL':40, 'XC':90, 'IV':4, 'IX':9}
        regular = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        i = 0
        ans = 0
        while i < len(s):
            if s[i:i+2] in special:
                ans += special[s[i:i+2]]
                i += 2
            elif s[i] in regular:
                ans += regular[s[i]]
                i += 1
        return ans