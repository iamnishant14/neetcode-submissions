class Solution:
    def maxArea(self, nums: List[int]) -> int:
        start,end = 0,len(nums)-1
        maxs= -1
        while start<end:
            current = min(nums[start],nums[end])*(end-start)
            maxs = max(maxs,current)
            print(maxs,start,end)
            if nums[start]<nums[end]:
                start+=1
            else:
                end-=1
        return maxs
