import collections
class Solution:
    def characterReplacement(self, s, k):
        alpha = [0 for _ in range(26)]
        ans = 0
        start = 0
        max_count = 0
        for end in range(len(s)):
            alpha[ord(s[end]) - ord('A')] += 1
            max_count = max(alpha)
            while end - start + 1 - max_count > k:
                alpha[ord(s[start]) - ord('A')] -= 1
                start += 1
            ans = max(ans, end - start + 1)
        return ans
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        