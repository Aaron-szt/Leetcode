# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        def getList(root, l=[]):
            if root.left:   getList(root.left, l)
            l.append(root.val)
            if root.right:  getList(root.right, l)
            return l
        l = getList(root)
        print(l)
        return l[k-1]