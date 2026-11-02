class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = set(nums)
        maxs = 0 
        for num in nums:
            if num-1 not in lcs:
                length=1
                while num+length in lcs:
                    length+=1
                maxs=max(maxs,length)
        return maxs
        