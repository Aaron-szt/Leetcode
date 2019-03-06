class Solution:
    def letterCombinations(self, digits):
        if digits == '':
            return []
        
        phone = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        used = {}
        
        def dfs(start, tmp, ans):
            if start == len(digits):
                ans.append(tmp)
                return ans
            for char in phone[digits[start]]:
                tmp += char
                ans = dfs(start + 1, tmp, ans)
                tmp = tmp[:-1]
            return ans
        return dfs(0, '', [])
        
        def dp(start, tmp, ans):
            if len(digits) == 1:
                return phone[digits[0]]
            for i in range(len(digits)-2, -1, -1):
                phone[digits[i:]] = []
                for ch1 in phone[digits[i]]:
                    tmp += ch1
                    for ch2 in phone[digits[i + 1:]]:
                        tmp += ch2
                        phone[digits[i:]].append(tmp)
                        if i == 0:
                            ans.append(tmp)
                        tmp = tmp[:-len(ch2)]
                    tmp = tmp[:-1]
            return ans
        return dp(0, '', [])
        
        
        """
        :type digits: str
        :rtype: List[str]
        """
        