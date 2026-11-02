class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start,end = 0,len(nums)-1
        while start<end:
            current_sum = nums[start]+nums[end]
            if current_sum == target:
                return [start+1,end+1]
            elif current_sum < target:
                start+=1
            else:
                end-=1
        return [start+1,end+1]
