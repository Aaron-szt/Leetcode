class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parans = []):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parans.append(p)
            return parans
        return generate('', n, n)