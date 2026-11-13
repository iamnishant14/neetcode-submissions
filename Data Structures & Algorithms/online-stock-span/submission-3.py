class StockSpanner:

    def __init__(self):
        self._stack = []
        

    def next(self, price: int) -> int:
        count = 1
        stack = self._stack
        while stack and stack[-1][0]<= price:
            count+=stack[-1][1]
            stack.pop()
        self._stack.append([price,count])
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)