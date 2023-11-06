# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return False
        else:
            return self.check(root.left, root.right)
    def check(self, l, r):
        if l == None and r == None:
            return True
        if l == None or r == None:
            return False
        if l.val == r.val:
            p = self.check(l.left, r.right)
            q = self.check(l.right, r.left)
            return p and q
        else:
            return False
        