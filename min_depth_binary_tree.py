# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth_dfs(self, root: TreeNode) -> int:
        if not root: return 0
        if not (root.left or root.right):
            return 1
        res = sys.maxsize
        if root.left:
            res = min(res, self.minDepth(root.left))
        if root.right:
            res = min(res, self.minDepth(root.right))
        return res + 1

    def minDepth_bfs(self, root):
        if not root: return 0

        q = [root]
        lvl = 1
        while q:
            q_nxt = []
            for node in q:
                if not (node.left or node.right):
                    return lvl
                if node.left:
                    q_nxt.append(node.left)
                if node.right:
                    q_nxt.append(node.right)

            q = q_nxt
            lvl += 1

        return lvl

    def minDepth(self, root):
        return self.minDepth_bfs(root)