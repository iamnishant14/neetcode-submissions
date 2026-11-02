class Solution:
    def getHours(self, piles,mid):
        total = 0
        for pile in piles:
            total += math.ceil(float(pile)/mid)
        return int(total)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxs = max(piles)
        start,end = 1, maxs
        res = end
        while start<=end:
            mid = start + (end-start)//2
            hours = self.getHours(piles,mid)
            if hours <= h:
                res = mid
                end = mid-1
            else:
                start = mid+1
        return res