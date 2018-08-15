class Solution:
    def tree2str(self, t):
        if not t:
            return ""
        result = str(t.val)
        if t.left:
            result += '(' + self.tree2str(t.left)  + ')'
            if t.right:
                result += '(' + self.tree2str(t.right)  + ')'
        elif t.right:
            result += '()' + '(' + self.tree2str(t.right)  + ')'
        return result