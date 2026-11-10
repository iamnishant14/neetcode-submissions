import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(-1.0 * float(x**2 + y**2),[x,y]) for x,y in points]
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        return [heap[index][1] for index in range(len(heap)-1,-1,-1)]
