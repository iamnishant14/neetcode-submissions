class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightSum = [0]*len(nums)
        currentProd = 1
        for i in range(len(nums)-1,-1,-1):
            rightSum[i]=currentProd
            currentProd*=nums[i]
        leftProd = 1
        out = list()
        for i in range(0,len(nums)):
            out.append(leftProd*rightSum[i])
            leftProd*=nums[i]
        return out
        