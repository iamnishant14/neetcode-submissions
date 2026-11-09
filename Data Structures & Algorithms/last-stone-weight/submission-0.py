import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [(-stone,stone) for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            last = heapq.heappop(heap)
            second = heapq.heappop(heap)
            rem = last[1] - second[1]
            if rem == 0:
                continue
            else:
                heapq.heappush(heap,(-rem,rem))
        return heap[0][1] if heap else 0