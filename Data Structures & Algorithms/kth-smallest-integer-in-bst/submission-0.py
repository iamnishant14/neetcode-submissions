# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kth(self, root, k, res):
        if not root:
            return
        self.kth(root.left, k, res)
        if k[0] == 0:
            return
        k[0] -= 1
        if k[0] == 0:
            res[0] = root.val
            return
        self.kth(root.right, k, res)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [root.val]
        self.kth(root, [k], res)
        return res[0]