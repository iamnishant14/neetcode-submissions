class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        maxs = 0
        rmax = [0]*len(height)
        rmax[len(height)-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            rmax[i]=max(height[i],rmax[i+1])
        lmax=height[0]
        for i in range(len(height)):
            lmax = max(height[i],lmax)
            maxs+= min(lmax,rmax[i]) - height[i]
        return maxs