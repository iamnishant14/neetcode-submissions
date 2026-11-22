class Deque:
    
    def __init__(self):
        self.arr = list()


    def isEmpty(self) -> bool:
        return not self.arr
        

    def append(self, value: int) -> None:
        self.arr.append(value)
        

    def appendleft(self, value: int) -> None:
        l = list()
        l.append(value)
        self.arr = l + self.arr
        

    def pop(self) -> int:
        if self.isEmpty(): return -1
        v = self.arr[-1]
        self.arr = self.arr[:-1]
        return v
        

    def popleft(self) -> int:
        if self.isEmpty(): return -1
        v = self.arr[0]
        self.arr = self.arr[1:]
        return v