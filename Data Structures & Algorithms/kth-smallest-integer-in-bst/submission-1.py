# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def dfs(node, k):
            nonlocal count

            if not node:
                return
            val = dfs(node.left, k)
            if val is not None:
                return val
            count += 1
            if count == k:
                return node.val
            val = dfs(node.right, k)
            if val is not None:
                return val
        return dfs(root, k)