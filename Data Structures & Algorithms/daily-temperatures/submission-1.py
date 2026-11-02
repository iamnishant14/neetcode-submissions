class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        res = [0]* len(temperatures)

        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            while stack and current_temp > stack[-1][0]:
                stackT,stackInd = stack.pop()
                res[stackInd] = i-stackInd
            stack.append((current_temp, i))
        return res