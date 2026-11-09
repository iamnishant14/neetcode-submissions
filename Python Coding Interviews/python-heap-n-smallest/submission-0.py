import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    heap = [num for num in arr]
    heapq.heapify(heap)
    return heap[0]


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    heap = [num for num in arr]
    heapq.heapify(heap)
    out = []
    count = 4
    while heap and count>0:
        out.append(heapq.heappop(heap))
        heapq.heapify(heap)
        count-=1
    return out


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    heap = [num for num in arr]
    heapq.heapify(heap)
    out,count = [],2
    while heap and count>0:
        out.append(heapq.heappop(heap))
        heapq.heapify(heap)
        count-=1
    return [out[index] for index in range(len(out)-1,-1,-1)]


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

