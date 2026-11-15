class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum = 0
        maxs = -sys.maxsize
        for index in range(len(nums)):
            lsum += nums[index]
            rsum = total - lsum + nums[index]
            maxs = max(maxs , max(lsum,rsum))
        return maxs
