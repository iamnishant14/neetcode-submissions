# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        current_sum = 0
        if not root:
            return False

        queue = deque()
        queue.append([root,root.val])

        while queue:
            curr,curr_sum = queue.popleft()
            if not curr.right and not curr.left:
                if curr_sum == targetSum:
                    return True
            if curr.right:
                queue.append([curr.right,curr_sum+curr.right.val])
            if curr.left:
                queue.append([curr.left,curr_sum+curr.left.val])
        return False