# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getlist(self, root, l):
        if not root:
            return 0
        self.getlist(root.left, l)
        l.append(root.val)
        self.getlist(root.right, l)
        
    

    def getMinimumDifference(self, root):
        l = []
        self.getlist(root, l)
        diff = abs(l[1] - l[0])
        for i in range(len(l)-1):
            if abs(l[i+1] - l[i]) < diff:
                diff = abs(l[i+1] - l[i])
        
        return diff
        
                 
        