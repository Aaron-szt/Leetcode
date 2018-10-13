# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def maxdepth(p):
            if not p: return 0
            left, right = maxdepth(p.left), maxdepth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        maxdepth(root)
        return self.ans
        """
        :type root: TreeNode
        :rtype: int
        """

