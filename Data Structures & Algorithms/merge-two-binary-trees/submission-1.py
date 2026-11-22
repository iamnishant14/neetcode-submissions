# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        queue = deque()
        queue.append([root1, root2])

        while queue:
            curr_a, curr_b = queue.popleft()
            if not curr_b:
                continue
            
            curr_a.val += curr_b.val
            
            if curr_a.left and curr_b.left:
                queue.append([curr_a.left, curr_b.left])
            elif not curr_a.left and curr_b.left:
                curr_a.left = curr_b.left
            
            if curr_a.right and curr_b.right:
                queue.append([curr_a.right, curr_b.right])
            elif not curr_a.right and curr_b.right:
                curr_a.right = curr_b.right
        return root1