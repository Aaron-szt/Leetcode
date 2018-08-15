class Solution:
    def lengthOfLongestSubstring(self, s):
        result = []
        s = list(s)
        i = 0
        while i < len(s):
            temp = []
            for j in range(i, len(s)):
                if s[j] not in temp:
                    temp += s[j]
                elif s[j] == temp[0]:
                    temp.pop(0)
                    temp += s[j]
                    i += 1
                else:
                    break
            if len(temp) > len(result):
                result = temp
            i += 1
        return len(result)

#The algorithm below is more beautiful!
used = {}
max_length = start = 0
for i, c in enumerate(s):
    if c in used and start <= used[c]:
        start = used[c] + 1
    else:
        max_length = max(max_length, i - start + 1)
            
    used[c] = i

return max_length