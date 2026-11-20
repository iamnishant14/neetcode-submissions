# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        root.val=0

        while queue:
            childs = [child for node in queue for child in (node.left,node.right) if child]
            total = sum(child.val for child in childs)
            for node in queue:
                sib = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = total - sib
                if node.right:
                    node.right.val = total - sib
            queue = childs
        return root

