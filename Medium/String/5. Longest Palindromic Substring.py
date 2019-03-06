class Solution:
    def longestPalindrome(self, s):
        def find(string, l, r, ans):
            if r < len(s) and len(ans) // 2 <= len(string) - r and len(ans) // 2 <= l + 1:
                while l >= 0 and r <= len(s) - 1 and string[l] == string[r]:
                    l -= 1
                    r += 1
                if string[l+1] == string[r-1] and r - l - 1 > len(ans):
                    return string[l + 1: r]
            return ans
        
        ans = ''
        if len(s) > 0:
            ans = s[0]
        
        for i in range(len(s)//2, -1, -1):
            ans = find(s, i, i + 1, ans)
            ans = find(s, i, i + 2, ans)
        for i in range(len(s)//2, len(s)):
            ans = find(s, i, i + 1, ans)
            ans = find(s, i, i + 2, ans)
        
        return ans
        
        """
        :type s: str
        :rtype: str
        """