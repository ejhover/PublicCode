# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        median = len(nums)//2
        nums[median] = TreeNode(nums[median])
        nums[median].left = self.sortedArrayToBST(nums[:median])
        nums[median].right = self.sortedArrayToBST(nums[median+1:])
        return nums[median]


p = Solution()
print(p.sortedArrayToBST([-10,-3,0,5,9]))
