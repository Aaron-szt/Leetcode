class Solution:
    def toGoatLatin(self, S):
        s = S.split()
        i = 0
        ans = ''
        while i < len(s):
            if s[i][0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',]:
                s[i] += 'ma'
            else:
                s[i] = s[i][1:] + s[i][0] + 'ma'
            for ii in range(i+1):
                s[i] += 'a'
            ans = ans + s[i] + ' '
            i += 1
        return ans[:-1]