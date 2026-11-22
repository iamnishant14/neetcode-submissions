class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        sys.setrecursionlimit(20000)
        tree = collections.defaultdict(list)
        for i in range(1, nodes):
            tree[parent[i]].append(i)
            
        def dfs(u):
            total_sum = value[u]
            total_count = 1
            for v in tree[u]:
                s, c = dfs(v)
                total_sum += s
                total_count += c
            if total_sum == 0:
                return 0, 0
            return total_sum, total_count
            
        return dfs(0)[1]