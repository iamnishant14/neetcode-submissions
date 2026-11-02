class MinStack:

    def __init__(self):
        self.arr = []
        self.mins = sys.maxsize
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.mins = min(self.mins, val)
        

    def pop(self) -> None:
        self.arr.pop()
        self.mins = self.arr[-1] if len(self.arr)> 0 else sys.maxsize
        for num in self.arr:
            self.mins = min(self.mins,num)
        

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mins
