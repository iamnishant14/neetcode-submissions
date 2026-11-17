# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        out = list()
        while queue:
            n = len(queue)
            curr = queue.popleft()
            if not curr:
                continue
            if not curr.left and curr.right:
                out.append(curr.right.val)
            if curr.left and not curr.right:
                out.append(curr.left.val)
            
            queue.append(curr.left)
            queue.append(curr.right)
        return out