class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = dict()
        out = list()
        for i in range(len(nums)):
            value = target-nums[i]
            if value in hashset:
                start,end = i,hashset[value]
                if start<end:
                    return [start,end]
                elif end<start:
                    return [end,start]
            else:
                hashset[nums[i]]=i