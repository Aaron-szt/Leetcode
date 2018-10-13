class Solution:
    def combine(self, n, k):
        visited = []
        self.ansT = []
        def dfs(n, k, now, tempAns):
            if len(tempAns) == k:
                self.ansT.append([])
                for x in tempAns:
                    self.ansT[-1].append(x)
                return
            for i in range(now, n+1):
                tempAns.append(i)
                dfs(n, k, i+1, tempAns)
                tempAns.pop()
            return self.ansT
        return dfs(n, k, 1, [])
        
        
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        