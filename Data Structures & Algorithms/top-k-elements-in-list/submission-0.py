class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
        sorted_nums = dict(sorted(hashmap.items(), key= lambda x: x[1]))
        return list(sorted_nums.keys())[len(sorted_nums)-k:]
        