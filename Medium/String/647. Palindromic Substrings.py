class Solution:
    def ifPalindromic(self, sub):
        return sub[::-1] == sub
    def countSubstrings(self, s):
        result = len(s)
        for i in range(len(s)):
            for ind in range(len(s)-1, i, -1):                
                if s[ind] == s[i]:
                    #print("s[ind]:", s[ind], "s[i]:", s[i])
                    result += self.ifPalindromic(s[i:ind+1])
                    #print("result:", result, "s[i:ind]: ", s[i:ind+1])
        return result
                    
        
#Center Expansion Idea!!!
class Solution:
    def countSubstrings(self, s):
        N = len(s)
        res = 0
        for center in range(2*N - 1):
            left = int(center / 2)
            right = int(left + center % 2)
            while left >= 0 and right < N and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

#Explaination:
#We perform a “center expansion” among all possible centers of the palindrome.
#Let N = len(S). There are 2N-1 possible centers for the palindrome: we could have a center at S[0], between S[0] and S[1], at S[1], between S[1] and S[2], at S[2], etc.
#To iterate over each of the 2N-1 centers, we will move the left pointer every 2 times, and the right pointer every 2 times starting with the second (index 1). Hence, left = center / 2, right = center / 2 + center % 2.
#From here, finding every palindrome starting with that center is straightforward: while the ends are valid and have equal characters, record the answer and expand.

#O(N) Solution! Using "Manacher's Algorithm"
def countSubstrings(self, S):
    def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        Z = [0] * len(A)
        center = right = 0
        for i in xrange(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i + Z[i]
        return Z

    return sum((v+1)/2 for v in manachers(S))