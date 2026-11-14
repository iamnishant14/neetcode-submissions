class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        out = 0
        for op in operations:
            if op =='+':
                sums = stack[-1]+stack[-2]
                stack.append(sums)
                out+=sums
            elif op == 'D':
                out+=stack[-1]*2
                stack.append(stack[-1]*2)
            elif op == 'C':
                rem = stack.pop()
                out-=rem
            else:
                out += int(op)
                stack.append(int(op))
        return out
        