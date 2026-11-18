# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        if not root:
            return False
        queue = deque([(root, 0)])
        while queue:
            curr, start = queue.popleft()
            if curr.val == arr[start]:
                if start == len(arr) - 1:
                    if curr.left is None and curr.right is None:
                        return True
                else:
                    if curr.left is not None:
                        queue.append((curr.left, start + 1))
                    if curr.right is not None:
                        queue.append((curr.right, start + 1))
        return False