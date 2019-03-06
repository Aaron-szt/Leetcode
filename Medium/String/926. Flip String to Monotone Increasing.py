class Solution:
    def minFlipsMonoIncr(self, S):
        left = False
        while len(S) > 0 and S[0] == '0':
            S = S[1:]
        if len(S) == 0:
            return 0
        zero = 0
        one = 0
        for i in S:
            if i == '0':
                zero += 1
            else:
                one += 1
            if zero > one:
                zero = one
        return zero