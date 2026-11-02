class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        result = [0]*len(t)
        stack = []

        for i,temp in enumerate(t):
            while stack and temp>stack[-1][0]:
                stackT,stackI = stack.pop()
                result[stackI] = i-stackI
            stack.append((temp,i))
        return result
        