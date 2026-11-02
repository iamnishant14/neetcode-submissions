# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        queue = list()
        queue.append(root)
        while len(queue) > 0:
            last_node = queue.pop(0)
            if val < last_node.val and last_node.left is not None:
                queue.append(last_node.left)
                continue
            elif val> last_node.val and last_node.right is not None:
                queue.append(last_node.right)
                continue
            elif val< last_node.val:
                last_node.left = TreeNode(val)
                break
            else:
                last_node.right = TreeNode(val)
                break
        return root
