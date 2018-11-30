class Solution:
    def fourSumCount(self, A, B, C, D):
        dicCD = {}
        ans = 0
        for c in C:
            for d in D:
                if c+d not in dicCD:
                    dicCD[c+d] = 1
                else:
                    dicCD[c+d] += 1
        
        for a in A:
            for b in B:
                if -a-b in dicCD:
                    ans += dicCD[-a-b]
        
        return ans
        