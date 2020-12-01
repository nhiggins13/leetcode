# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode, level=0) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left, level + 1)
        right = self.maxDepth(root.right, level + 1)

        return 1 + max(left, right)

