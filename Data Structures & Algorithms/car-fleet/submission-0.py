class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Position: [4,1,0,7] and speed : [2,2,1,1]

        Let's sort the position and speed based on respective position.

        position: [0,1,4,7] speed: [1,2,2,1]
        target = 10
        remaining: [10,9,6,3]

        for cars on left to catch up , distance should be same at any given time

        so for example :

        t1 -> position: [1,3,6,8]
        t2 -> pos: [2,5,8,10]
        t3 -> pos: [3,7,10,10]

        so at Tx time , pos = [1+1*(tx),1+2*tx,4+2*tx,7+1*tx]
        7+tx = 4+2tx
        tx = 3
        tx = (target - pos[x])/speed[x]
        """

        stack = []
        pair = [(pos,speed) for pos,speed in zip(position,speed)]
        pair.sort(reverse=True)

        for pos,speed in pair:
            stack.append((target -pos)/speed)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
