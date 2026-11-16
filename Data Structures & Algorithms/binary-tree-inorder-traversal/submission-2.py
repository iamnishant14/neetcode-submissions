# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self,root,out):
        if not root:
            return 
        self.inOrder(root.left,out)
        out.append(root.val)
        self.inOrder(root.right,out)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = list()
        self.inOrder(root,out)
        return out
        