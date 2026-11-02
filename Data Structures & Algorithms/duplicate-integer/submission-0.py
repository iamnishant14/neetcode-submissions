class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num]=hashmap.get(num,0)+1
        return False
         