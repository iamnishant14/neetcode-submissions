class StockSpanner:

    def __init__(self):
        self._stack = []
        

    def next(self, price: int) -> int:
        count = 1
        stack = self._stack.copy()
        while stack and stack[-1] <= price:
            count+=1
            stack.pop()
        self._stack.append(price)
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)