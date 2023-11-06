class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
global ans
ans = 1
class Solution:
    def maxDepth(self, root, ans=1) -> int:
        if not root:
            return 0
        if root.left == None and root.right == None:
            return ans
        elif root.left == None and root.right != None:
            return self.maxDepth(root.right, ans+1)
        elif root.left != None and root.right == None:
            return self.maxDepth(root.left, ans+1)
        elif root.left != None and root.right != None:
            return max(self.maxDepth(root.right, ans+1), self.maxDepth(root.left, ans+1))
'''        ans = 1
        if not root:
            return 0
        return self.helper(root.left, root.right, ans)
    def helper(self, left, right, depth): # (none, 2, 1) (None, None, 2)
        if left == None and right == None:
            return depth
        elif left == None and right != None:
            return self.helper(right.left, right.right, depth + 1)
        elif left != None and right == None:
            return self.helper(left.left, left.right, depth + 1)
        elif left != None and right != None:
            return max(self.helper(right.left, right.right, depth + 1), self.helper(left.left, left.right, depth + 1))'''
def main():
    p = Solution()
    print(p.maxDepth(TreeNode(1, None, TreeNode(2))))
if __name__ == "__main__":
    main()