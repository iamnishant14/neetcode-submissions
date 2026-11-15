class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums)!=len(set(nums)):
            return False
        n = len(nums)
        mins = min(nums)
        ranges = (mins,mins+n-1)
        for num in nums:
            if ranges[0]<=num<=ranges[1]:
                continue
            else:
                return False
        return True