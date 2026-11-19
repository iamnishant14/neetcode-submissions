# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        min_val , max_val = 0, 0
        vertical = defaultdict(list)
        queue = deque([(root,0)])

        while queue:
            curr,counter = queue.popleft()
            min_val = min(min_val,counter)
            max_val = max(max_val,counter)
            vertical[counter].append(curr.val)

            if curr.left:
                queue.append((curr.left,counter-1))
            if curr.right:
                queue.append((curr.right,counter+1))
        out = list()
        for index in range(min_val,max_val+1):
            out.append(vertical[index])
        return out