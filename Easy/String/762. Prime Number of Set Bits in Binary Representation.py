class Solution:
    def countPrimeSetBits(self, L, R):
        Prime = [2,3,5,7,11,13,17,19,23]
        ans = 0
        for num in range(L, R+1):
            if bin(num)[2:].count('1') in Prime:
                ans += 1
        return ans