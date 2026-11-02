import sys
class MinStack:

    def __init__(self):
        self._stack = list()
        self._min = sys.maxsize

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._min > val:
            self._min = val

    def pop(self) -> None:
        if self._stack:
            self._stack.pop()
        self._eval_min()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min
    
    def _eval_min(self):
        self._min = min(self._stack) if self._stack else sys.maxsize
