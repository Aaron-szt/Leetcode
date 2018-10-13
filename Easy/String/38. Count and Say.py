class Solution:
    def countAndSay(self, n):
        s = '1'
        for _ in range(n-1):
            s = ''.join(str(len(list(group))) + digit  for digit, group in itertools.groupby(s))
        return s
        
        
        
        # inpt = '1'
        # for nn in range(n-1):
        #     i = 0
        #     ans = ''
        #     while i < len(inpt):
        #         count = 1
        #         while len(inpt) - i > 1:
        #             if inpt[i] == inpt[i+1]:
        #                 count += 1
        #                 i += 1
        #             else:   break
        #         ans = ans + str(count) + inpt[i]
        #         i += 1
        #     inpt = ans
        # return inpt    
                    
        """
        :type n: int
        :rtype: str
        """
        