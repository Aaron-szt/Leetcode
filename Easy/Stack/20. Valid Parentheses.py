class Solution:
    def isValid(self, s):
        left = ['(', '[', '{']
        right = {')':'(', ']':'[', '}':'{'}
        i = 0
        stack = []
        while i < len(s):
            if s[i] in left:
                stack.append(s[i])
                i += 1
            elif s[i] in right and stack != []:
                if stack[-1] == right[s[i]]:
                    stack.pop()
                    i += 1
                else:   return False
            else: return False
        if stack == []:
            return True
        return False
        
        # i = 0
        # stack = []
        # for i in s:
        #     if i == '(':
        #         stack.append(')')
        #     elif i == '[':
        #         stack.append(']')
        #     elif i == '{':
        #         stack.append('}')
        #     elif stack == [] or stack.pop() != i:
        #         return False
        # return stack == []
            
        """
        :type s: str
        :rtype: bool
        """
        