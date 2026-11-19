# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = dict()
        if not root:
            return []
        q = deque()

        if root:
            q.append((0, root))
        while len(q) > 0:
            
            curr_step, curr = q.popleft()
            if curr_step not in h:
                h[curr_step] = []
            h[curr_step].append(curr.val)
            if curr.left:
                q.append((curr_step - 1, curr.left))
            if curr.right:
                q.append((curr_step + 1, curr.right))
        return [h[k] for k in range(min(h.keys()), max(h.keys())+1)]
        