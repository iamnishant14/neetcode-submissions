class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        queues = deque()
        queues.append(root)

        while queues:
            n = len(queues)
            for index in range(n):
                curr = queues.popleft()
                if curr == u:
                    if index == n - 1:
                        return None
                    else:
                        return queues.popleft()
                if curr.left:
                    queues.append(curr.left)
                if curr.right:
                    queues.append(curr.right)
        return None