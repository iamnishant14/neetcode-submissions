class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = list()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            start,end = i+1,len(nums)-1
            while start<end:
                current = nums[start]+nums[end] + nums[i]
                if current == 0:
                    trips.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                    while nums[start]==nums[start-1] and start<end:
                        start+=1
                elif current<0:
                    start+=1
                else:
                    end-=1
        return trips 

        