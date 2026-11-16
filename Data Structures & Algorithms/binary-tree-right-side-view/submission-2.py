# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deques = deque()
        out = list()
        if root:
            deques.append(root)
        else:
            return out
        while deques:
            size = len(deques)
            for index in range(size):
                current = deques.popleft()
                if index == size - 1:
                    out.append(current.val)
                if current.left:
                    deques.append(current.left)
                if current.right:
                    deques.append(current.right)
        return out