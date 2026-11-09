import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._heap = nums
        self._counter = k
        heapq.heapify(self._heap)
        while len(self._heap) > self._counter:
            heapq.heappop(self._heap)

    def add(self, val: int) -> int:
        heapq.heappush(self._heap, val)
        if len(self._heap) > self._counter:
            heapq.heappop(self._heap)
        return self._heap[0]

