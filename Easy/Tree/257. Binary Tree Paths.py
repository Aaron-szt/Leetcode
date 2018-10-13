# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs + stack
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        ans = []
        stack = [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                ans.append(ls + str(node.val))
            if node.left:
                stack.append((node.left, ls + str(node.val) + '->'))
            if node.right:
                stack.append((node.right, ls + str(node.val) + '->'))
        
        return ans
    
# bfs + queue
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        ans = []
        queue = collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                ans.append(ls + str(node.val))
            if node.left:
                queue.append((node.left, ls + str(node.val) + '->'))
            if node.right:
                queue.append((node.right, ls + str(node.val) + '->'))
        
        return ans
    
# dfs recursively
class Solution:
    def binaryTreePaths(self, root):
        ans = []
        s = ''
        def paths(p, s, ans):           
            if not p.left and not p.right:
                ans.append(s + str(p.val))
            if p.left:
                paths(p.left, s + str(p.val) +'->', ans)
            if p.right:
                paths(p.right, s + str(p.val) +'->', ans)
            
        if root:        
            paths(root, s, ans)
        return ans