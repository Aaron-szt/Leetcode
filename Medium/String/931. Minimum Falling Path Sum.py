class Solution:
    def minFallingPathSum(self, A):
        
        def bottom_up(tmp, rows, cols):
            mini = 2 ** 31 -1
            for r in range(rows - 2, -1, -1):
                for c in range(cols):
                    tmp_min = 2 ** 31 - 1
                    for bia in [-1, 0, 1]:
                        if (c + bia) >= 0 and (c + bia) < cols:
                            tmp_min = min(tmp_min, A[r + 1][c + bia])
                    A[r][c] += tmp_min

            for c in range(cols):
                mini = min(mini, A[0][c])

            return mini
                    
        
        rows = len(A)
        cols = len(A[0])
        last = -1
        mini = 2 ** 31 - 1
        tmp = 0
        row = 0
        return bottom_up(tmp, rows, cols)