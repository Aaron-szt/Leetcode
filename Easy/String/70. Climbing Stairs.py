class Solution:
    def factorial(self, m):
        if m == 0:
            return 1
        else:
            return m*self.factorial(m-1)
        
    def climbStairs(self, n):
        result = 0
        for i in range(n//2 + 1):
            result += self.factorial(n-i) / (self.factorial(n-2*i) * self.factorial(i))
        return int(result)

#这尼玛是个斐波那契？？？？？
def climbStairs(self, n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a