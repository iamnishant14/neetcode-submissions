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
            for index in range(n):
                curr = queue.popleft()
                if curr.left and curr.right:
                    queue.append(curr.left)
                    queue.append(curr.right)
                elif curr.left:
                    queue.append(curr.left)
                    out.append(curr.left.val)
                elif curr.right:
                    queue.append(curr.right)
                    out.append(curr.right.val)
                else:
                    continue
        return out