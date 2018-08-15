class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n-1):
            let, count, temp = s[0], 0, ''
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    count = 1
                    let = l
            temp += str(count)+let
            s = temp
        return s
                    